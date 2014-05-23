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
from third_part.alipay_dual.alipay_api import *

def index(request):
    template_name = 'templates/zhifu_dual.html'
    return render_to_response(template_name)

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        out_trade_no = request.POST.get('out_trade_no', '')
        subject = request.POST.get('subject', '')
        price = request.POST.get('price', '')

        quantity = request.POST.get('quantity', '')
        logistics_fee = request.POST.get('logistics_fee', '')
        logistics_type = request.POST.get('logistics_type', '')
        logistics_payment = request.POST.get('logistics_payment', '')

        body = request.POST.get('body', '')
        show_url = request.POST.get('show_url', '')

        receive_name = request.POST.get('receive_name', '')
        receive_address = request.POST.get('receive_address', '')
        receive_zip = request.POST.get('receive_zip', '')
        receive_phone = request.POST.get('receive_phone', '')
        receive_mobile = request.POST.get('receive_mobile', '')

        html = '<p>订单已经提交，准备进入支付宝官方收银台 ...</p>'
        submit = Alipay_API()
        html = submit.alipay_submit(out_trade_no, subject, price, \
                        quantity, logistics_fee, logistics_type, logistics_payment, \
                        body, show_url, \
                        receive_name, receive_address, receive_zip, receive_phone, receive_mobile)

    return HttpResponse(html)

def return_url(request):            # 支付宝同步通知跳转url，get 方式
    out_trade_no = request.GET.get('out_trade_no', '')
    trade_no = request.GET.get('trade_no', '')          # 支付宝交易号
    trade_status = request.GET.get('trade_status', '')
    price = request.GET.get('price', '')

    if trade_status == 'WAIT_SELLER_SEND_GOODS' or trade_status == 'TRADE_FINISHED':
        # // 支付宝返回的支付成功状态
        # // 可以再次加入平台的订单处理逻辑代码，如记录数据库，提供用户一下必要的服务信息等
        # // 注意：如果是异步通知的url，还可以根据订单号对数据库中的订单进行查询，判断是否已经处理了？

        # todo ...
        logResult('============ 双功能 同步通知 ===============')
        logResult('订单号：' + out_trade_no)
        logResult('支付宝交易号：' + trade_no)
        logResult('订单费用：' + price)
        logResult('==========================================')


    return HttpResponse('订单购买成功！')

def notify_url(request):            # 支付宝异步通知url，post 方式
    out_trade_no = request.POST.get('out_trade_no', '')
    trade_no = request.POST.get('trade_no', '')
    trade_status = request.POST.get("trade_status", '')

    if trade_status == 'WAIT_BUYER_PAY':  # 表示买家已在支付宝交易管理中产生了交易记录，但没有付款
        # todo ...
        pass
    elif trade_status == 'WAIT_SELLER_SEND_GOODS':  # 表示买家已在支付宝交易管理中产生了交易记录且付款成功，但卖家没有发货
        # todo ...
        pass
    elif trade_status == 'WAIT_BUYER_CONFIRM_GOODS':  # 表示卖家已经发了货，但买家还没有做确认收货的操作
        # todo ...
        pass
    elif trade_status == 'TRADE_FINISHED':  # 表示买家已经确认收货，这笔交易完成
        # todo ...
        pass

    # // Todo...
    logResult('============ 异步通知 ===============')
    logResult('订单号：' + out_trade_no)
    logResult('支付宝交易号：' + trade_no)
    logResult('====================================')

    return HttpResponse('success')  # donnot modify this

def logResult(msg):  # 写日志，方便测试（看网站需求，也可以改成把记录存入数据库）
    log = 'third_part/alipay_direct/log_dual.txt'
    fi = open(log, 'a')
    fi.write(msg + "\n")
    fi.close()
