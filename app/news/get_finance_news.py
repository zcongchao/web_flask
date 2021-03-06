#coding:utf-8
import cons as ct
import news_vars as nv
import pandas as pd
import numpy as np
from datetime import datetime
import lxml.html
from lxml import etree
import re
import json
#from ..celery_created import celery
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

import os
import time
from celery import Celery
import eventlet
from ..__init__ import app

eventlet.monkey_patch()
app.config.from_pyfile( 'celeryconfig.py' ) #os.path.join(here, 'proj/）
celery = Celery(app.name)
celery.conf.update(app.config)


def guba_sina(show_content=False):
    """
       获取sina财经股吧首页的重点消息
    Parameter
    --------
        show_content:是否显示内容，默认False
    
    Return
    --------
    DataFrame
        title, 消息标题
        content, 消息内容（show_content=True的情况下）
        ptime, 发布时间
        rcounts,阅读次数
    """
    
    from pandas.io.common import urlopen
    print nv.GUBA_SINA_URL%(ct.P_TYPE['http'],
                                       ct.DOMAINS['sina'])
    try:
        with urlopen(nv.GUBA_SINA_URL%(ct.P_TYPE['http'],
                                       ct.DOMAINS['sina'])) as resp:
            lines = resp.read()
        html = lxml.html.document_fromstring(lines)
        res = html.xpath('//ul[@class=\"list_05\"]/li[not (@class)]')
        heads = html.xpath('//div[@class=\"tit_04\"]')
        data = []
        for head in heads:
            title = head.xpath('a/text()')[0]
            url = head.xpath('a/@href')[0]
            ds = [title]
            ds.extend(_guba_content(url))
            data.append(ds)
        for row in res:
            title = row.xpath('a[2]/text()')[0]
            url = row.xpath('a[2]/@href')[0]
            ds = [title]
            ds.extend(_guba_content(url))
            data.append(ds)
        df = pd.DataFrame(data, columns=nv.GUBA_SINA_COLS)
        df['rcounts'] = df['rcounts'].astype(float)
        return df if show_content is True else df.drop('content', axis=1)
    except Exception as er:
        print(str(er))  
    
    
def _guba_content(url):
    try:
        html = lxml.html.parse(url)
        res = html.xpath('//div[@class=\"ilt_p\"]/p')
        if ct.PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr).replace('&#12288;', '')#.replace('\n\n', '\n').
        html_content = lxml.html.fromstring(sarr)
        content = html_content.text_content()
        ptime = html.xpath('//div[@class=\"fl_left iltp_time\"]/span/text()')[0]
        rcounts = html.xpath('//div[@class=\"fl_right iltp_span\"]/span[2]/text()')[0]
        reg = re.compile(r'\((.*?)\)') 
        rcounts = reg.findall(rcounts)[0]
        return [content, ptime, rcounts]
    except Exception:
        return ['', '', '0']

@celery.task
def add(x, y):
    return x + y

if __name__ == "__main__":
    datas=guba_sina(show_content=True)
    datas = np.array(datas)
    datas = datas.tolist()
    for data in datas:
        print data[0]

"""
celery -A app.news.get_finance_news.celery -P eventlet worker -l info --pool=solo

from app.news.get_finance_news import guba_sina
result = guba_sina.delay(show_content=True)

In [10]: result
<AsyncResult: a52aab9e-a8c1-4ef0-a7cb-511a6b46a2e6>

In [11]: result.ready()
True

In [12]: result.get()
"""

