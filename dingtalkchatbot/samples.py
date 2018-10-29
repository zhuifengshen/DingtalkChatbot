#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 15/01/2018 17:08
__author__ = 'Devin -- http://zhangchuzhao.site'
import json
import logging
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, FeedLink, CardItem

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    # *************************************这里填写自己钉钉群自定义机器人的token*****************************************
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=52d9034cc78680bc0d4ba6a65748e77fa7b96ee43d57b96116910606f7863d59'
    # 用户手机号列表
    at_mobiles = ['*************************这里填写需要提醒的用户的手机号码，字符串或数字都可以****************************']
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)
    # text
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', is_at_all=True)
    xiaoding.send_text(msg='我就是小丁，小丁就是我！', at_mobiles=at_mobiles)

    # image表情
    xiaoding.send_image(pic_url='http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png')

    # link
    xiaoding.send_link(title='万万没想到，某小璐竟然...', text='故事是这样子的...', message_url='http://www.kwongwah.com.my/?p=454748", pic_url="https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg')

    # markdown
    # 1、提醒所有人
    xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                           '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                           '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                           '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                           is_at_all=True)
    # 2、提醒指定手机用户，需要在text参数中@用户
    xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                           '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                           '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                           '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                           at_mobiles=at_mobiles)

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
    card1 = CardItem(title="氧气美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    card2 = CardItem(title="氧眼美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    card3 = CardItem(title="氧神美女", url="https://www.dingtalk.com/", pic_url="https://unzippedtv.com/wp-content/uploads/sites/28/2016/02/asian.jpg")
    cards = [card1, card2, card3]
    xiaoding.send_feed_card(cards)


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
