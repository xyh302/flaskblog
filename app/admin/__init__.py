from flask_admin import Admin
from app.admin.admin import MyHomeView, UserView, PostView,\
    ArticleView, MyView
from app.models import User, Post, Article


def create_admin(app=None):
    admin = Admin(app, name=u'后台管理系统', index_view=MyHomeView(),
                  base_template='admin/my_master.html')
    admin.add_view(UserView(User))
    admin.add_view(PostView(Post))
    admin.add_view(ArticleView(Article))
