from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from app.models import User
from werkzeug.security import check_password_hash


class AdminForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])

    def get_user(self):
        user = User.objects(username=self.username.data).first()
        if user is not None:
            if not check_password_hash(user.password_hash,
                                       self.password.data):
                return None
            if not user.is_admin:
                return None
            return user
        else:
            return None