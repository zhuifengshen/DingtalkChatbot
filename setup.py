#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import io
import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command

"""
打包步骤：
1、功能逻辑编码和测试完成；
2、更新 __about__.py 中版本号；
3、提交代码至仓库；
4、构建打包：python setup.py upload
"""

about = {}
here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'dingtalkchatbot', '__about__.py'), encoding='utf-8') as f:
    exec(f.read(), about)

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()

install_requires = ["requests"]


class UploadCommand(Command):
    """ Build and publish this package.
        Support setup.py upload. Copied from requests_html.
    """

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in green color."""
        print("\033[0;32m{0}\033[0m".format(s))

    def initialize_options(self):
        """ override
        """
        pass

    def finalize_options(self):
        """ override
        """
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
            rmtree(os.path.join(here, 'DingtalkChatbot.egg-info'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Publishing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


setup(
    name=about['__title__'],
    version=about['__version__'],
    packages=find_packages(),
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    keywords='钉钉 机器人 dingtalk chatbot robot bot',
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    # python setup.py upload
    cmdclass={
        'upload': UploadCommand
    }
)
