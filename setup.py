#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# create time: 13/01/2018 20:41
import io
from setuptools import setup

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

with io.open("requirements.txt", encoding='utf-8') as f:
    install_requires = f.readlines()

setup(
    name="DingtalkChatbot",
    version="1.1.2",
    description="DingtalkChatbot is a Python wrapper tool for dingtalk custom chatbot messages.",
    long_description=long_description,
    author="Devin Zhang",
    author_email="1324556701@qq.com",
    url="https://github.com/zhuifengshen/DingtalkChatbot",
    license='MIT',
    keywords='dingtalk dingding chatbot robot bot',
    install_requires=install_requires,
    setup_requires=['setuptools'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)