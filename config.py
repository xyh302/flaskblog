import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random-event'

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'blog',
        'host': '127.0.0.1',
        'port': 27017
    }
