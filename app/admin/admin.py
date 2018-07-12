from flask_admin import BaseView, expose, AdminIndexView
from flask import redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.admin.forms import AdminForm
from flask_admin.contrib.mongoengine import ModelView

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,\
    ValidationError
from wtforms.validators import DataRequired, EqualTo
from app.models import User


class CreateUserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('再次输入密码', validators=[DataRequired(),
                                                    EqualTo('password')])
    isAdmin = BooleanField(default=False)

    def validate_username(self, field):
        if User.objects(username=field.data).first():
            raise ValidationError('用户名已存在')


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated and current_user.is_admin:
            return super(MyHomeView, self).index()
        return redirect(url_for('admin.login'))

    @expose('/login', methods=['GET', 'POST'])
    def login(self):
        form = AdminForm()
        if form.validate_on_submit():
            user = form.get_user()
            if user == None:
                return redirect(url_for('admin.login'))
            elif user is not None:
                login_user(user)
                return redirect(url_for('admin.index'))
        self._template_args['form'] = form
        return super(MyHomeView, self).index()

    @expose('/logout')
    def logout(self):
        user = current_user
        if current_user.is_authenticated:
            logout_user()
        return redirect(url_for('admin.index'))


class UserView(ModelView):
    column_filters = ['username']
    column_exclude_list = ['password_hash']

    can_delete = True
    can_view_details = True
    can_create = True
    can_edit = True

    form_excluded_columns = ['password_hash']

    edit_template = 'admin/blog_edit.html'
    create_template = 'admin/blog_create.html'
    list_template = 'admin/blog_list.html'

    form = CreateUserForm

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class PostView(ModelView):
    can_delete = True
    can_view_details = True
    can_create = False
    can_edit = False
    column_exclude_list = ['author']
    list_template = 'admin/blog_list.html'

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class ArticleView(ModelView):
    can_delete = True
    can_view_details = True
    can_create = False
    can_edit = False
    column_exclude_list = ['author', 'article_id']
    list_template = 'admin/blog_list.html'

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin


class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'hello, world'