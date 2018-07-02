from app.article import bp
from flask_login import login_required, current_user
from app.article.forms import ArticleForm
from app.models import Article
from flask import render_template, flash, redirect, url_for
from datetime import datetime
from app.models import User


@bp.route('/new_acticle', methods=['GET', 'POST'])
@login_required
def new_article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data,
                          content=form.content.data,
                          author=User.objects(
                              username=current_user.username).first(),
                          author_name=current_user.username,
                          create_time=datetime.utcnow())
        article.save()
        flash('发布成功')
        return redirect(url_for('main.index'))
    return render_template('article/new_article.html',
                           title='写文章', form=form)

@bp.route('/article/<string:article_id>', methods=['GET'])
def article_detail(article_id=''):
    article = Article.objects(id=article_id).first()
    return render_template('article/article_detail.html',
                           article=article)