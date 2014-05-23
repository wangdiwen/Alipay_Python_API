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
from third_part.alipay_direct.alipay_api import *

def index(request):
    template_name = 'templates/zhifu.html'
    return render_to_response(template_name)

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        out_trade_no = request.POST.get('out_trade_no', '')
        subject = request.POST.get('subject', '')
        total_fee = request.POST.get('total_fee', '')
        body = request.POST.get('body', '')
        show_url = request.POST.get('show_url', '')

        html = '<p>订单已经提交，准备进入支付宝官方收银台 ...</p>'
        submit = Alipay_API()
        html = submit.alipay_submit(out_trade_no, subject, total_fee, body, show_url)

    return HttpResponse(html)

def return_url(request):            # 支付宝同步通知跳转url，get 方式
    out_trade_no = request.GET.get('out_trade_no', '')
    trade_no = request.GET.get('trade_no', '')          # 支付宝交易号
    trade_status = request.GET.get('trade_status', '')
    total_fee = request.GET.get('total_fee', '')

    if trade_status == 'TRADE_SUCCESS' or trade_status == 'TRADE_FINISHED':
        # // 支付宝返回的支付成功状态
        # // 可以再次加入平台的订单处理逻辑代码，如记录数据库，提供用户一下必要的服务信息等
        # // 注意：如果是异步通知的url，还可以根据订单号对数据库中的订单进行查询，判断是否已经处理了？

        # todo ...
        logResult('============ 同步通知 ===============')
        logResult('订单号：' + out_trade_no)
        logResult('支付宝交易号：' + trade_no)
        logResult('订单费用：' + total_fee)
        logResult('====================================')


    return HttpResponse('订单购买成功！')

def notify_url(request):            # 支付宝异步通知url，post 方式
    out_trade_no = request.POST.get('out_trade_no', '')
    trade_no = request.POST.get('trade_no', '')
    trade_status = request.POST.get("trade_status", '')

    if trade_status == 'TRADE_SUCCESS' or trade_status == 'TRADE_FINISHED':
        # // TRADE_SUCCESS 交易状态只在一种情况下出现——开通了高级即时到账，买家付款成功后。
        # // 说明：状态的逻辑按照我们平台开通的服务决定？

        # // Todo：网站平台一般在此做一些逻辑处理，比如：判断订单数据库中是否已经对改订单号进行了处理了？
        # // 因为在同步通知url中会提前做业务处理，使用在此做判断，是为了保险起见。

        # // Todo...
        logResult('============ 异步通知 ===============')
        logResult('订单号：' + out_trade_no)
        logResult('支付宝交易号：' + trade_no)
        logResult('====================================')

    return HttpResponse('success')

def logResult(msg):  # 写日志，方便测试（看网站需求，也可以改成把记录存入数据库）
    log = 'third_part/alipay_direct/log.txt'
    fi = open(log, 'a')
    fi.write(msg + "\n")
    fi.close()
