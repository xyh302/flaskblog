from flask import render_template, url_for, redirect, flash, request
from app.auth.forms import LoginForm, RegisterForm
from app.auth import bp
from app.models import User
from flask_login import current_user, login_user, logout_user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is not None and \
            user.check_password(form.password.data):
            login_user(user)
            flash('欢迎登录')
            print(current_user.username)
            print(current_user.is_authenticated)
            return redirect(url_for('main.index'))
        flash('无效的用户名或密码')
    return render_template('auth/login.html', form=form, title='登录')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        new_user.save()
        flash('注册成功')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form, title='注册')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))