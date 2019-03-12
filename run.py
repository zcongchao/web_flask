#!/usr/bin/env python3
# encoding: utf-8


from app import create_app
from app.models import ArticleType, article_types, Source, \
    Comment, Article, User, Menu, ArticleTypeSetting, BlogInfo, \
    Plugin, BlogView

app = create_app()

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


if __name__ == '__main__':
    app.run('0.0.0.0', 5000,debug=True)
