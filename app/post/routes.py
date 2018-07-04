from app.post import bp
from app.post.forms import PostForm, CommentForm
from flask import request, current_app, flash, render_template, \
    redirect, url_for
from flask_login import login_required, current_user
from app.models import User, Post, Comment
from datetime import datetime
import os
from werkzeug.security import generate_password_hash


@bp.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = Post(content=form.content.data,
                        author=User.objects(username=current_user.username).first(),
                        author_name=current_user.username,
                        create_time=datetime.utcnow())
            if request.files['pic']:
                pic = request.files['pic']
                fname = pic.filename
                ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
                UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER']
                if not (os.path.isdir(os.path.join(UPLOAD_FOLDER))):
                    os.mkdir(os.path.join(UPLOAD_FOLDER))
                if not (os.path.isdir(os.path.join(UPLOAD_FOLDER,
                                                   current_user.username))):
                    os.mkdir(os.path.join(UPLOAD_FOLDER,
                                          current_user.username))
                flag = '.' in fname and \
                       fname.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
                if not flag:
                    flash('错误的文件类型')
                    return render_template('post/new_post.html',
                                           form=form)
                pic.save('{}{}/{}'.format(UPLOAD_FOLDER,
                                          current_user.username,
                                          fname))   #linux目录
                post.pic = '/static/post_pic/{}/{}'.format(
                    current_user.username, fname)
            post.save()
            flash('发布成功')
            return redirect(url_for('post.post_view'))
    return render_template('post/new_post.html',
                               form=form, title='发微博')


@bp.route('/post_view')
def post_view():
    User.objects(username=current_user.username).first().update(
        last_seen=datetime.utcnow())
    page_num = request.args.get('page', 1, type=int)
    posts = Post.objects.order_by('-create_time').paginate(
        page=page_num, per_page=3
    )
    return render_template('post/post_view.html',
                           posts=posts, title='微博列表')


@bp.route('/post_detail/<string:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.objects(id=post_id).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data,
                          comment_id=generate_password_hash(form.content.data),
                          author=User.objects(username=current_user.username).first(),
                          author_name=current_user.username,
                          create_time=datetime.utcnow())
        post.comments.append(comment)
        post.save()
        return redirect(url_for('post.post_detail', post_id=post.id))
    return render_template('post/post_detail.html',
                           title='微博全文', post=post, form=form)