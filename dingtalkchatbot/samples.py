#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 15/01/2018 17:08
__author__ = 'Devin -- http://zhangchuzhao.site'
import json
import logging
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, FeedLink, CardItem

logging.basicConfig(level=logging.ERROR)


# def mini_sample():
#     webhook = 'https://oapi.dingtalk.com/robot/send?access_token=这里填写自己钉钉群自定义机器人的token'
#     at_mobiles = ['这里填写需要提醒的用户的手机号码，字符串或数字都可以']
#     headers = {'Content-Type': 'application/json; charset=utf-8'}
#     post_data = {
#         'msgtype': 'text',
#         'text': {
#             'content': '我就是小丁，小丁就是我！'
#         },
#         'at': {
#             'atMobiles': at_mobiles,
#             'isAtAll': False
#         }
#     }
#     r = requests.post(webhook, headers=headers, data=json.dumps(post_data))
#     print(r.content)  # 输出消息发送结果


if __name__ == '__main__':
    # *************************************这里填写自己钉钉群自定义机器人的token*****************************************
    # 一、旧版的钉钉自定义机器人（无需安全设置）
    old_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=77eb420ff2761ad516d974e1428c3e198b84faabc9c9ef8e86b2c71ac60bd0ea'
    # 二、新版的钉钉自定义机器人必须配置安全设置（自定义关键字、加签、IP地址/段），其中“加签”需要传入密钥才能发送成功
    new_webhook = 'https://oapi.dingtalk.com/robot/send?access_token=aa62d3aa55cd785609d1de1b8c82ebc0d5a106aa5983833ed15023cef80db7fa'
    secret = 'SEC11b94b27f5953b94deee33840d2863ebfbe7c75b68848613cdbd80228752d63b'  # 创建机器人时钉钉设置页面有提供
    # 用户手机号列表
    at_mobiles = ['18825166XXX', '这里填@的人的手机号，可自定义@的位置，默认添加在消息末尾']
    
    # 初始化机器人小丁
    # xiaoding = DingtalkChatbot(old_webhook)  # 旧版初始化方式
    
    # 新版安全设置为“加签”时，需要传入请求密钥
    # 同时支持设置消息链接跳转方式，默认pc_slide=False为跳转到浏览器，pc_slide为在PC端侧边栏打开
    # 同时支持设置消息发送失败时提醒，默认fail_notice为false不提醒，开发者可以根据返回的消息发送结果自行判断和处理
    xiaoding = DingtalkChatbot(new_webhook, secret=secret, pc_slide=True, fail_notice=False)
    
    # text
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', is_at_all=True)
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', at_mobiles=at_mobiles)

    # # image
    xiaoding.send_image(pic_url='http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg')

    # link
    xiaoding.send_link(title='万万没想到，某小璐竟然...',
                       text='故事是这样子的...',
                       message_url='http://www.kwongwah.com.my/?p=454748', 
                       pic_url='https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')

    # markdown
    # 1、提醒所有人
    xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                           '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                           '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                           '> ###### 10点20分发布 [天气](https://www.seniverse.com/) \n',
                           is_at_all=True)
    # 2、提醒指定手机用户，并在text内容中自定义”@用户“的位置
    xiaoding.send_markdown(title='氧气文字', text='#### 广州天气 @18825166XXX\n'
                           '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                           '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                           '> ###### 10点20分发布 [天气信息](https://www.seniverse.com/)\n',
                           at_mobiles=at_mobiles, is_auto_at=False)

    # 整体跳转ActionCard
    btns1 = [CardItem(title="查看详情", url="https://www.dingtalk.com/")]
    actioncard1 = ActionCard(title='万万没想到，竟然...',
                             text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                             btns=btns1,
                             btn_orientation=1,
                             hide_avatar=1)
    xiaoding.send_action_card(actioncard1)

    # 单独跳转ActionCard
    # 1、两个按钮选择
    btns2 = [CardItem(title="支持", url="https://www.dingtalk.com/"), CardItem(title="反对", url="https://www.dingtalk.com/")]
    actioncard2 = ActionCard(title='万万没想到，竟然...',
                             text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                             btns=btns2,
                             btn_orientation=1,
                             hide_avatar=1)
    xiaoding.send_action_card(actioncard2)
    # 2、三个按钮选择
    btns3 = [CardItem(title="支持", url="https://www.dingtalk.com/"), CardItem(title="中立", url="https://www.dingtalk.com/"), CardItem(title="反对", url="https://www.dingtalk.com/")]
    actioncard3 = ActionCard(title='万万没想到，竟然...',
                             text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                             btns=btns3,
                             btn_orientation=1,
                             hide_avatar=1)
    xiaoding.send_action_card(actioncard3)

    # FeedCard类型
    card1 = CardItem(title="氧气美女", url="https://www.baidu.com/", pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
    card2 = CardItem(title="氧眼美女", url="https://www.baidu.com/", pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
    card3 = CardItem(title="氧神美女", url="https://www.baidu.com/", pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg")
    cards = [card1, card2, card3]
    xiaoding.send_feed_card(cards)
