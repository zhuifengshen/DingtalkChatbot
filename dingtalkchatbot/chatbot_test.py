#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 16/01/2018 14:37
import unittest

from dingtalkchatbot.chatbot import DingtalkChatbot, is_not_null_and_blank_str, ActionCard, FeedLink, CardItem

__author__ = 'Devin - https://zhuifengshen.github.io'

class TestDingtalkChatbot(unittest.TestCase):
    """DingtalkChatbot 测试用例"""

    @classmethod
    def setUpClass(cls):
        # 1.无加签
        cls.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=77eb420ff2761ad516d974e1428c3e198b84faabc9c9ef8e86b2c71ac60bd0ea'
        cls.xiaoding = DingtalkChatbot(cls.webhook)
        # 2.有加签
        #cls.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=fab4f070e0214d2e3f7429acd18bc38848cc7043f9191ed1f96fa090ab25b943'
        #cls.xiaoding = DingtalkChatbot(cls.webhook, secret='SEC225443235b43d49959eaca83b15b5b93ec747d662ad347a2b3483a7e67d8b96b')


    def test_is_not_null_and_blank_str(self):
        """测试字符串不为空函数"""
        self.assertFalse(is_not_null_and_blank_str(''), 'pass')
        self.assertFalse(is_not_null_and_blank_str(' '), 'pass')
        self.assertFalse(is_not_null_and_blank_str('   '), 'pass')
        self.assertTrue(is_not_null_and_blank_str('abc'), 'pass')
        self.assertTrue(is_not_null_and_blank_str('123'), 'pass')

    def test_send_text(self):
        """测试发送文本消息函数"""
        result = self.xiaoding.send_text(msg='我就是小丁，小丁就是我！', is_at_all=True)
        self.assertEqual(result['errcode'], 0)

    def test_send_image(self):
        """测试发送表情图片消息函数"""
        result = self.xiaoding.send_image(pic_url='http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg')
        self.assertEqual(result['errcode'], 0)

    def test_send_link(self):
        """测试发送链接消息函数"""
        result = self.xiaoding.send_link(title='万万没想到，某小璐竟然...', text='故事是这样子的...', message_url='https://open.dingtalk.com/document/group/custom-robot-access', pic_url='http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png')
        self.assertEqual(result['errcode'], 0)

    def test_send_markdown(self):
        """测试发送Markdown格式消息函数"""
        result = self.xiaoding.send_markdown(title='氧气文字', text='#### 广州天气\n'
                                                  '> 9度，西北风1级，空气良89，相对温度73%\n\n'
                                                  '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
                                                  '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
                                             is_at_all=True)
        self.assertEqual(result['errcode'], 0)

    def test_send_actioncard(self):
        """1.测试发送整体跳转ActionCard消息功能(基于CardItem新API)"""
        btns1 = [CardItem(title="查看详情", url="https://open.dingtalk.com/document/group/custom-robot-access")]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard1)
        self.assertEqual(result['errcode'], 0)

        """2.测试发送单独跳转ActionCard消息功能(基于CardItem新API)"""
        btns2 = [CardItem(title="支持", url="https://www.dingtalk.com/"), CardItem(title="反对", url="https://www.baidu.com/")]
        actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard2)
        self.assertEqual(result['errcode'], 0)

    def test_send_actioncard_old_api(self):
        """ 1.测试发送整体跳转ActionCard消息功能(基于字典旧API)"""
        btns1 = [{"title": "查看详情", "actionURL": "https://www.dingtalk.com/"}]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard1)
        self.assertEqual(result['errcode'], 0)

        """2.测试发送单独跳转ActionCard消息功能(基于字典旧API)"""
        btns2 = [{"title": "支持", "actionURL": "https://www.dingtalk.com/"},
                 {"title": "反对", "actionURL": "https://www.baidu.com/"}]
        actioncard2 = ActionCard(title='万万没想到，竟然...',
                                 text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns2,
                                 btn_orientation=1,
                                 hide_avatar=1)
        result = self.xiaoding.send_action_card(actioncard2)
        self.assertEqual(result['errcode'], 0)

    def test_send_feedcard(self):
        """测试发送FeedCard类型消息功能（基于CardItem新API)"""
        carditem1 = CardItem(title="氧气美女", url="https://www.dingtalk.com/", pic_url="http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg")
        carditem2 = CardItem(title="氧眼美女", url="https://www.dingtalk.com/", pic_url="http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png")
        carditem3 = CardItem(title="氧神美女", url="https://www.dingtalk.com/", pic_url="http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png")
        cards = [carditem1, carditem2, carditem3]
        result = self.xiaoding.send_feed_card(cards)
        self.assertEqual(result['errcode'], 0)

    def test_send_feedcard_old_api(self):
        """测试发送FeedCard类型消息功能(基于FeedLink旧API)"""
        feedlink1 = FeedLink(title="氧气美女", message_url="https://www.dingtalk.com/", pic_url="http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg")
        feedlink2 = FeedLink(title="氧眼美女", message_url="https://www.dingtalk.com/", pic_url="http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png")
        feedlink3 = FeedLink(title="氧神美女", message_url="https://www.dingtalk.com/", pic_url="http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png")
        links = [feedlink1, feedlink2, feedlink3]
        result = self.xiaoding.send_feed_card(links)
        self.assertEqual(result['errcode'], 0)


if __name__ == '__main__':
    unittest.main()
