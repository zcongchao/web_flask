# coding=utf-8
import os
import time
from celery import Celery
import eventlet
from .__init__ import app

eventlet.monkey_patch()
app.config.from_pyfile( 'celeryconfig.py' ) #os.path.join(here, 'proj/）
celery = Celery(app.name)
celery.conf.update(app.config)


"""
def creat_celery():
    app.config.from_pyfile( 'celeryconfig.py' )
    celery = Celery(app.name)
    celery.conf.update(app.config)
    return celery

celery = creat_celery()
"""

