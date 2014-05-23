#!/usr/bin/env python
#coding=utf-8

# Note:
#     支付宝 双功能 API

from alipay_config import *
from alipay_submit import *
from alipay_notify import *

class Alipay_API:
    payment_type = "1"          # 支付类型
    return_url = "http://192.168.1.199:8000/dual/return"      # 页面跳转同步通知页面路径
    notify_url = "http://192.168.1.199:8000/dual/notify"      # 服务器异步通知页面路径
    seller_email = ''                                                       # 卖家支付宝帐户
    anti_phishing_key = ""      # 防钓鱼时间戳
    exter_invoke_ip = ""        # 客户端的IP地址

    alipay_config = ''

    def __init__(self):
        alipay_config = Alipay_Config()

        self.seller_email = alipay_config.seller_email
        self.partner = alipay_config.partner
        self.key = alipay_config.key
        self.sign_type = alipay_config.sign_type
        self.input_charset = alipay_config.input_charset
        self.cacert = alipay_config.cacert
        self.transport = alipay_config.transport

    # out_trade_no: 商户订单号, 商户网站订单系统中唯一订单号，必填
    # subject: 订单名称
    # price: 付款金额
    # quantity: 商品数量，必填，建议默认为1，不改变值，把一次交易看成是一次下订单而非购买一件商品
    # logistics_fee: 物流费用
    # logistics_type: 物流类型, 必填，三个值可选：EXPRESS（快递）、POST（平邮）、EMS（EMS）
    # logistics_payment: 物流支付方式, 必填，两个值可选：SELLER_PAY（卖家承担运费）、BUYER_PAY（买家承担运费）
    # body: 订单描述
    # show_url: 商品展示地址, 需以http://开头的完整路径
    # receive_name: 收货人姓名
    # receive_address: 收货人地址
    # receive_zip: 收货人邮编
    # receive_phone: 收货人电话号码
    # receive_mobile: 收货人手机号码
    def alipay_submit(self, out_trade_no, subject, price, \
                            quantity, logistics_fee, logistics_type, logistics_payment, \
                            body, show_url, \
                            receive_name, receive_address, receive_zip, receive_phone, receive_mobile):
        parameter = {
            'service': "trade_create_by_buyer",
            'partner': self.partner,
            'payment_type': Alipay_API.payment_type,
            'notify_url': Alipay_API.notify_url,
            'return_url': Alipay_API.return_url,

            'seller_email': self.seller_email,
            'out_trade_no': out_trade_no,
            'subject': subject,
            'price': price,

            'quantity': quantity,
            'logistics_fee': logistics_fee,
            'logistics_type': logistics_type,
            'logistics_payment': logistics_payment,

            'body': body,
            'show_url': show_url,

            'receive_name': receive_name,
            'receive_address': receive_address,
            'receive_zip': receive_zip,
            'receive_phone': receive_phone,
            'receive_mobile': receive_mobile,

            '_input_charset': self.input_charset,
        }
        submit = AlipaySubmit()
        html_text = submit.buildRequestForm(parameter, 'get', '确定')
        return html_text


    def get_notify(self):
        notify = AlipayNotify()
        return notify.verifyReturn()   # True/False
