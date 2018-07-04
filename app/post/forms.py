from flask_wtf import FlaskForm
from wtforms import TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    content = TextAreaField('微博内容', validators=[DataRequired()])
    pic = FileField()
    submit = SubmitField('发布')


class CommentForm(FlaskForm):
    content = TextAreaField('评论', validators=[DataRequired()])
    submit = SubmitField('发布')
