#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 13/01/2018 20:41
import io
from setuptools import setup
from dingtalkchatbot import __version__

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

with io.open("requirements.txt", encoding='utf-8') as f:
    install_requires = f.readlines()

setup(
    name="DingtalkChatbot",
    version=__version__,
    description="DingtalkChatbot is a Python wrapper tool for dingtalk custom chatbot messages.",
    long_description=long_description,
    author="Devin Zhang",
    author_email="1324556701@qq.com",
    url="https://github.com/zhuifengshen/DingtalkChatbot",
    license='MIT',
    keywords='dingtalk chatbot',
    install_requires=install_requires,
    setup_requires=['setuptools']
)