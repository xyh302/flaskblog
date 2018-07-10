from flask import Blueprint

bp = Blueprint('article_main', __name__)

from app.article import routes

