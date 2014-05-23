#!/usr/bin/env python
#coding=utf-8

# import python env
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# import django env
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from third_part.alipay_send.alipay_api import *

def index(request):
    template_name = 'templates/send_zhifu.html'
    return render_to_response(template_name)

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        trade_no = request.POST.get('trade_no', '')
        logistics_name = request.POST.get('logistics_name', '')
        invoice_no = request.POST.get('invoice_no', '')
        transport_type = request.POST.get('transport_type', '')

        html = ''
        submit = Alipay_API()
        html = submit.alipay_submit(trade_no, logistics_name, invoice_no, transport_type)

        # here, just for testing
        # XML DATA like this:
        # <?xml version="1.0" encoding="utf-8"?>
        # <alipay><is_success>F</is_success><error>ILLEGAL_PARTNER_EXTERFACE</error></alipay>

        print html
        logResult('============= 商家发货确认 日志 ================')
        logResult(html)
        logResult('===============================================')

        # 注意： 这里的 html 为支付宝官方返回的 XML 文本数据，需要解析 XML，
        #        获取 XML 节点中的 ‘alipay’ 第一个value
        # 请在这里加上商户的业务逻辑程序代码
        # 请根据业务逻辑来编写程序（以下代码仅作参考
        # 获取支付宝的通知返回参数，可参考技术文档中页面跳转同步通知参数列表

        alipay_node_value = ''  # 解析xml数据, todo ...

    return HttpResponse(alipay_node_value)


def logResult(msg):  # 写日志，方便测试（看网站需求，也可以改成把记录存入数据库）
    log = 'third_part/alipay_send/log.txt'
    fi = open(log, 'a')
    fi.write(msg + "\n")
    fi.close()
