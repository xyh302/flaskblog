from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('文章内容', validators=[DataRequired()])
    submit = SubmitField('发布')