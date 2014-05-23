#!/usr/bin/env python

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# import django env
from django.conf.urls import patterns, include, url

# import web site modles
from controllers import test, zhifu, dual_zhifu, send_zhifu

# urls conf
urlpatterns = patterns('',  # init instance
    # test urls
    url(r'^test/$', test.test),

    # dual func, trade create by user
    url(r'^dual/submit$', dual_zhifu.submit),
    url(r'^dual/return$', dual_zhifu.return_url),
    url(r'^dual/notify$', dual_zhifu.notify_url),
    url(r'^dual/$', dual_zhifu.index),

    # dual func, send goods confirm by platform
    url(r'^send/submit$', send_zhifu.submit),
    url(r'^send/$', send_zhifu.index),

    # direct func, create direct pay by user
    url(r'^submit$', zhifu.submit),
    url(r'^return$', zhifu.return_url),
    url(r'^notify$', zhifu.notify_url),
    url(r'^$', zhifu.index),
)
