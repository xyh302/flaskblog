from flask_login import UserMixin
from werkzeug.security import check_password_hash, \
    generate_password_hash
from .extensions import db


class User(UserMixin, db.Document):
    username = db.StringField(required=True)
    password_hash = db.StringField(required=True)
    isAdmin = db.BooleanField(default=False)
    last_seen = db.DateTimeField()
    love = db.ListField(db.StringField())
    meta = {
        'collection': 'user',
        'strict': False
    }

    @property
    def password(self):
        raise AttributeError('无权限')

    @property
    def is_admin(self):
        return self.isAdmin

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Article(db.Document):
    meta = {
        'collection': 'article',
    }
    title = db.StringField(required=True)
    content = db.StringField(required=True)
    author = db.ReferenceField(User)
    author_name = db.StringField(required=True)
    create_time = db.DateTimeField()

    def __repr__(self):
        return "<Article> {}".format(self.title)


class Post(db.Document):
    meta = {
        'collection': 'post',
    }
    content = db.StringField(required=True)
    pic = db.StringField()
    author = db.ReferenceField(User)
    author_name = db.StringField(required=True)
    create_time = db.DateTimeField()
    comments = db.EmbeddedDocumentListField('Comment')
    liked_by = db.ListField(db.StringField())

    def __repr__(self):
        return "<Post> {}".format(self.content)


class Comment(db.EmbeddedDocument):
    comment_id = db.StringField(max_length=250, required=True)
    content = db.StringField(required=True)
    author = db.ReferenceField(User)
    author_name = db.StringField(required=True)
    create_time = db.DateTimeField()

    def __repr__(self):
        return "<Comment> {}".format(self.content)
