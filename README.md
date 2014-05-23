Alipay_Python_API
=================

This repo is Python API interface of Alipay, it gives direct and dual trade 2 functions.

Note:
=================
这个仓库是支付宝接口的 Python 版本，提供了即时到帐和双功能（担保交易）2种功能。

其中 Web 项目基于 Django，

支付宝接口功能的 API 和 Lib 在项目结构目录的 third_part 目录中，

1、alipay_direct ==> 即时到帐功能接口

2、alipay_dual   ==> 双功能（担保交易）功能接口

3、alipay_send   ==> 商家物流发货确认功能接口（配合双功能使用）


关于接口类：
==================
每个功能都是独立的给出简洁的 API 接口，在每个功能目录的下面，有个叫 alipay_api.py 的 Python 文件，

里面定义了 Alipay_API 这个接口类，接口类提供统一的调用接口 alipay_submit，

alipay_submit 接口便是买家订单的提交入口，在项目的 application/zhi/controllers/ 下面的 zhi/dual_zhi/send_zhi/.py 脚本中可以作为参考。


关于如何集成使用 Alipay_Python_API：
==================
1、商家支付宝账户配置：

在 third_part/ 下面的每个独立功能中，找到 alipay_config.py ，在 Alipay_Config 类中，定义自己的商家支付宝账户信息：包括 seller_email、partner、key

2、配置你自己的处理支付宝返回 URL：

在 third_part/ 下面的每个独立功能中，找到 alipay_api.py，在 Alipay_API 类中，找到 return_url、notify_url，改为你自己的 Web 服务器处理 URL.

3、接口获取订单提交：
在 application/zhi/controllers/ 下面 zhi/dual_zhi/send_zhi/.py 脚本，可以作为参考。
接口使用只需要 2 行代码：

1-1、New 一个订单提交对象

submit = Alipay_API()

1-2、提交订单，获取支付宝官方的 HTML 表单内容

html = submit.alipay_submit()



运行项目：
==================
# python2.7 manager.py runserver 0.0.0.0:8000

或者使用项目中给出的 uwsgi 方式开启 Web 服务器，但是要求你的服务器上面已经提供了 uwsgi 程式；

# uwsgi --http 0.0.0.0:8000 --chdir /opt/www/mysite/mysite/ --module django_uwsgi


浏览器验证：
==================
1、即时到帐功能

浏览器输入 url http://192.168.1.199:8000

2、双功能（担保交易）

浏览器输入 url http://192.168.1.199:8000/dual

3、商家物流发货确认

浏览器输入 url http://192.168.1.199:8000/send



关于本 SDK 项目：
===================
这份支付宝商家集成 Python API，以及 Django 简单的集成 Demo 项目，是在帮助一位朋友做支付宝集成的过程中开发而来，

当初在集成的过程中，发现支付宝官方并没有提供商家支付宝交易的 Python SDK，而在网上，我也没有找到合适的 Alipay Python API，而 Github 上面已经有不少国内的开发者提供了一些开源版本，但是大都单独提供 Lib 或者 Python 代码，很少有提供完整的基于 Django 或者其他 Web Python 框架的实际生产 Demo，

所以我自己根据支付宝官方的文档 《即时到帐交易接口（create_direct_pay_by_user）接入与使用规则》、《标准双接口（trade_create_by_buyer）接入与使用规则）、《确认发货接口（send_goods_confirm_by_platform）接入与使用规则》，开发了这个 Alipay Python SDK，

在 Django 项目的 third_part 第三方目录里面，你可以找到对应的支付宝功能目录 SDK，

在开发的过程中，我也借鉴了支付宝官方提供的 demo 中的 PHP 接口实现，其中大部分的类、方法，在 Python 接口中都与 PHP 的方法一致，如果你也是一位同时熟悉 PHP 和 Python 开发者的话，相信自己在研究 third_part 下面代码的时候，会发现这一点，

此份 SDK 和配套的 Django 项目实际生产 Demo，如果说它做的比较好一点的地方，就是它不仅给出了易于使用的 Class API，而且同时给出了一个在 Web 生产环境下面使用的 Django Demo。


关于作者：
=====================
Steven Wang，

如果你碰巧使用了这份 SDK、发现了 Bug、或者想学习和交流的话，

欢迎与我联系: dw_wang126@126.com

Good Luck!
