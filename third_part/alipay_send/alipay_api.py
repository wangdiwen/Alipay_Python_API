#!/usr/bin/env python
#coding=utf-8

# Note:
#     支付宝 API

from alipay_config import *
from alipay_submit import *
from alipay_notify import *

class Alipay_API:
    payment_type = "1"          # 支付类型
    seller_email = ''           # 卖家支付宝帐户
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

    # trade_no: 支付宝交易号
    # logistics_name: 物流公司名称
    # invoice_no: 物流发货单号
    # transport_type: 物流运输类型
    def alipay_submit(self, trade_no, logistics_name, invoice_no, transport_type):
        parameter = {
            'service': "send_goods_confirm_by_platform",

            'partner': self.partner,
            'trade_no': trade_no,
            'logistics_name': logistics_name,
            'invoice_no': invoice_no,
            'transport_type': transport_type,

            '_input_charset': self.input_charset,
        }
        submit = AlipaySubmit()
        html_text = submit.buildRequestHttp(parameter)
        return html_text


    def get_notify(self):
        notify = AlipayNotify()
        return notify.verifyReturn()   # True/False
