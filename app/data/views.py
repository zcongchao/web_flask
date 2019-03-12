#coding:utf-8

from flask import render_template, request, current_app, redirect,\
    url_for, flash, jsonify
from . import data
from ..models import PasteFile
from .. import db
import redis
import json
import redis
import msgpack

r = redis.StrictRedis(host='localhost', port=6379, db=6)
MAX_FILE_COUNT = 50

def default(obj):
    if isinstance(obj, PasteFile):
        return msgpack.ExtType(42, obj.to_dict())
    raise TypeError('Unknown type: %r' % (obj,))


def ext_hook(code, data):
    if code == 42:
        p = PasteFile.from_dict(data)
        return p
    return msgpack.ExtType(code, data)




@data.route('/upload', methods=['POST'])
def upload():
    #更新数据视图
    name = request.form.get('name')

    pastefile = PasteFile(name)
    db.session.add(pastefile)
    db.session.commit()
    p = PasteFile.query.get(pastefile.id)
    packed = msgpack.packb(p,default=default)
    r.lpush('latest.files', packed)
    r.ltrim('latest.files', 0, MAX_FILE_COUNT - 1)

    return jsonify({'r': 0})


@data.route('/lastest_files')
def get_lastest_files():
    start = request.args.get('start', default=0, type=int)
    limit = request.args.get('limit', default=20, type=int)
    ids = r.lrange('latest.files', start, start + limit - 1)
    files = [msgpack.unpackb(pak, ext_hook=ext_hook) for pak in ids]
    return json.dumps([{'id': f.id, 'filename': f.name, 'uploadtime': str(f.uploadtime)} for f in files])

"""
In [3]: import time

In [4]: import random

In [5]: import string

In [6]: with app.test_client() as client:
   ...:     for _ in range(100):
   ...:         client.post('/data/upload', data={'name':"".join(random.sample(string.ascii_letters, 10))})
   ...:         time.sleep(0.5)
   ...:         
"""
