一、钉钉自定义机器人介绍
==========================

钉钉机器人是钉钉群的一个高级扩展功能，但使用起来却非常简单，只需要注册一个钉钉账号，就可以将第三方服务信息聚合到钉钉群中，实现信息的自动同步。

常见的使用场景：

1、聚合Github、Gitlab等源码管理服务，实现源码更新同步；

2、聚合Trello、JIRA等项目协调服务，实现项目信息同步；

3、机器人支持Webhook自定义接入，就可以实现更多可能性，例如：将运维报警、自动化测试结果报告、工作&生活日程安排（上班打卡、下班吃饭、健身、读书、生日、纪念日...）的提醒；

目前自定义机器人支持文本（text）、链接（link）、markdown三种消息格式，五种消息类型，详细信息请参考\ `自定义机器人官方文档 <https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq>`__

二、安装使用
============

这么好用的功能，只要在钉钉群中添加机器人，得到Webhoo地址即可。接下来，我们先在命令行终端一睹为快吧：

::

    curl 'https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d '
      {"msgtype": "text",
        "text": {
            "content": "我就是我, 是不一样的烟火"
         }
      }'

由于各种消息调用，官方只提供Java语言的封装，平时使用Python比较多，为了更方便平时自动化项目的使用，周末花了点时间用Python语言对各种消息类型进行了一一封装，代码已开源在GitHub上，同时也上传了PyPI。

| 1、项目源码地址如下：\ `DingtalkChatbot <https://github.com/zhuifengshen/DingtalkChatbot>`__
| 2、安装和更新命令如下：

::

    pip install DingtalkChatbot
    pip install -U DingtalkChatbot

3、支持功能如下：

-  支持Text消息；
-  支持Link消息；
-  支持image表情消息；
-  支持Markdown消息；
-  支持ActionCard消息；
-  支持消息发送失败时自动通知（默认fail_notice=False不通知，开发者可根据返回的消息发送结果自行判断处理）
-  支持设置消息链接打开方式（默认pc_slide=False，跳转至浏览器打开，pc_slide=True，则在PC端侧边栏打开）
-  支持钉钉官方消息发送频率限制限制：每个机器人每分钟最多发送20条；
-  支持Python2、Python3；
-  支持钉钉企业内部机器人\ `自定义outgoing机器人消息发送 <https://ding-doc.dingtalk.com/doc#/serverapi2/elzz1p>`__；
-  支持最新版钉钉机器人加密设置密钥验证；

三、各消息类型使用示例
======================

|image0|

.. code:: python

    from dingtalkchatbot.chatbot import DingtalkChatbot
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=这里填写自己钉钉群自定义机器人的token'
    secret = 'SEC11b9...这里填写自己的加密设置密钥'  # 可选：创建机器人勾选“加签”选项时使用
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
    xiaoding = DingtalkChatbot(webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）
    # Text消息@所有人
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', is_at_all=True)

|image1|

.. code:: python

    # Text消息之@指定用户
    at_mobiles = ['这里填写需要提醒的用户的手机号码，字符串或数字都可以']
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', at_mobiles=at_mobiles)


|image9|

.. code:: python

    # image表情消息
    xiaoding.send_image(pic_url='http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png')


|image2|

.. code:: python

    # Link消息
    xiaoding.send_link(title='万万没想到，李小璐竟然...', text='故事是这样子的...', message_url='http://www.kwongwah.com.my/?p=454748", pic_url="https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')

|image3|

.. code:: python

    # Markdown消息@所有人
    xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                               '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                               '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                               '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                               is_at_all=True)

|image4|

.. code:: python

        # Markdown消息@指定用户
        xiaoding.send_markdown(title='氧气文字', text='#### 广州天气 @18825166128\n'
                               '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                               '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                               '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                               at_mobiles=at_mobiles)

|image5|

.. code:: python

    # FeedCard消息类型（注意：当发送FeedCard时，pic_url需要传入参数值，必选）
    card1 = CardItem(title="氧气美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    card2 = CardItem(title="氧眼美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    card3 = CardItem(title="氧神美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    cards = [card1, card2, card3]
    xiaoding.send_feed_card(cards)

|image6|

.. code:: python

    # ActionCard整体跳转消息类型
    btns1 = [CardItem(title="查看详情", url="https://www.dingtalk.com/")]
    actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![选择](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
    xiaoding.send_action_card(actioncard1)

|image7|

.. code:: python

    # ActionCard独立跳转消息类型（双选项）
    btns2 = [CardItem(title="支持", url="https://www.dingtalk.com/"), CardItem(title="反对", url="https://www.dingtalk.com/")]
    actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![选择](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
    xiaoding.send_action_card(actioncard2)

|image8|

.. code:: python

    # ActionCard独立跳转消息类型（列表选项）
    btns3 = [CardItem(title="支持", url="https://www.dingtalk.com/"), CardItem(title="中立", url="https://www.dingtalk.com/"), CardItem(title="反对", url="https://www.dingtalk.com/")]
    actioncard3 = ActionCard(title='万万没想到，竟然...',
                                 text='![选择](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns3,
                                 btn_orientation=1,
                                 hide_avatar=1)
    xiaoding.send_action_card(actioncard3)


四、常见注意事项
===========================

-  1、at_mobiles列表上的手机号默认自动添加到消息文本末尾，可将参数改为is_auto_at=False取消自动化添加，在消息文本自定义@的位置，支持同时@多个手机号，以便突出对应的人去关注对应的内容；
-  2、图片链接是Http，在网页版钉钉无法正常显示，在客户端则可以，需要更改为使用Https；
-  3、消息链接打开方式可以在初始化机器人时设置（默认pc_slide=False，跳转至浏览器打开，pc_slide=True，则在PC端侧边栏打开）；



**哥们，更多使用场景，现在尽情展开想象吧...**

（如果对你有帮助的话，欢迎**star**）

.. |image0| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/text_at_all.png
.. |image1| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/text_at_one.png
.. |image2| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/link.png
.. |image3| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/markdown_at_all.png
.. |image4| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/markdown_at_one.png
.. |image5| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/feedcard.png
.. |image6| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/global_actioncard.png
.. |image7| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/select_actioncard.png
.. |image8| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/multi_actioncard.png
.. |image9| image:: https://raw.githubusercontent.com/zhuifengshen/DingtalkChatbot/master/img/image_msg.png
