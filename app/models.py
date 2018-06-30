from app import db, login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, \
    generate_password_hash

@login.user_loader
def load_user(username):
    return User.objects(username=str(username)).first()

class User(db.Document, UserMixin):
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

