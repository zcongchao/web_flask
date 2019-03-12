#!/usr/bin/env python
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import app , db#create_app
from app.models import ArticleType, article_types, Source, \
    Comment, Article, User, Menu, ArticleTypeSetting, BlogInfo, \
    Plugin, BlogView
#from flask_soc import app


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# Global variables to jiajia2 environment:
app.jinja_env.globals['ArticleType'] = ArticleType
app.jinja_env.globals['article_types'] = article_types
app.jinja_env.globals['Menu'] = Menu
app.jinja_env.globals['BlogInfo'] = BlogInfo
app.jinja_env.globals['Plugin'] = Plugin
app.jinja_env.globals['Source'] = Source
app.jinja_env.globals['Article'] = Article
app.jinja_env.globals['Comment'] = Comment
app.jinja_env.globals['BlogView'] = BlogView


def make_shell_context():
    return dict(db=db, ArticleType=ArticleType,Source=Source,
                Comment=Comment, Article=Article, User=User, Menu=Menu,
                ArticleTypeSetting=ArticleTypeSetting, BlogInfo=BlogInfo,
                Plugin=Plugin, BlogView=BlogView)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy(deploy_type):
    from flask_migrate import upgrade
    from app.models import BlogInfo, User, ArticleTypeSetting, Source, \
        ArticleType, Plugin, BlogView, Comment

    # upgrade database to the latest version
    upgrade()

    if deploy_type == 'product':
        # step_1:insert basic blog info
        BlogInfo.insert_blog_info()
        # step_2:insert admin account
        User.insert_admin(email='798422668@163.com', username='zoucongchao', password='6964433zou')
        # step_3:insert system default setting
        ArticleTypeSetting.insert_system_setting()
        # step_4:insert default article sources
        Source.insert_sources()
        # step_5:insert default articleType
        ArticleType.insert_system_articleType()
        # step_6:insert system plugin
        Plugin.insert_system_plugin()
        # step_7:insert blog view
        BlogView.insert_view()

if __name__ == '__main__':
    manager.run()
