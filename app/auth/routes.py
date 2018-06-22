from flask import render_template
from .forms import LoginForm
from . import bp

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='登录')
