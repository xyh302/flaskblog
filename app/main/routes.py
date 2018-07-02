from app.main import bp
from flask import render_template
from flask_login import current_user, login_required
from datetime import datetime
from app.models import User, Article

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        current_user.save()

@bp.route('/')
@bp.route('/index')
def index():
    user = {'username': 'Miguel'}
    articles = Article.objects.all().order_by('-create_time')
    return render_template('index.html', user=user, articles=articles)


# @bp.route('/user/<username>')
# @login_required
# def user(username):
#     user = User.objects(username=username).first()
#     posts = [
#         {'author': user, 'body': 'Test post #1'},
#         {'author': user, 'body': 'Test post #2'}
#     ]
#     return render_template('user.html', user=user, posts=posts)
#
