#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@author: blossom_zhang
@license: 
@contact: blossom_zhang@163.com
@software: 
@file: setup.py
@time: 2017/12/13 13:59
@desc:
'''

from setuptools import setup, find_packages
from wechat import VERSION

url="https://github.com/jeffkit/wechat"

long_description="Wechat Python SDK"

setup(name="wechat",
      version=VERSION,
      description=long_description,
      maintainer="blossom_zhang",
      maintainer_email="blossom_zhang@163.com",
      url = url,
      long_description=long_description,
      install_requires = ['requests'],
      packages=find_packages('.'),
     )