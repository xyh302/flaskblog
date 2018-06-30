from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('再次输入密码', validators=[DataRequired(),
                                                EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        if User.objects(username=username.data).first():
            raise ValidationError('用户名已存在')


