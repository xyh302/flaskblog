from flask import Blueprint

bp = Blueprint('post_main', __name__)

from app.post import routes