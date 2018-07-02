from app import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, \
    generate_password_hash


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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(uid):
    print('call load_user')
    u = User.objects.with_id(uid)
    print(u)
    return u


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