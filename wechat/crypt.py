#!/usr/bin/env python

# -*- coding: utf-8 -*-
# @author  : Free_zhang
# @license :
# @email   : blossom_zhang@163.com
# @software:
# @file    : crypt.py
# @time    : 2017/12/13 22:05
# @desc    :

import base64
import string
import random
import hashlib
import time
import struct
from Crypto.Cipher import AES
import xml.etree.cElementTree as ET
import sys
import socket

WXBizMsgCrypt_OK = 0
WXBizMsgCrypt_ValidateSignature_Error = -40001
WXBizMsgCrypt_ParseXml_Error = -40002
WXBizMsgCrypt_ComputeSignature_Error = -40003
WXBizMsgCrypt_IllegalAesKey = -40004
WXBizMsgCrypt_ValidateAppidOrCorpid_Error = -40005
WXBizMsgCrypt_EncryptAES_Error = -40006
WXBizMsgCrypt_DecryptAES_Error = -40007
WXBizMsgCrypt_IllegalBuffer= -40008
WXBizMsgCrypt_EncodeBase64_Error= -40009
WXBizMsgCrypt_DecodeBase64_Error = -40010
WXBizMsgCrypt_GenRetrunXml_Error = -40011

"""
关于Crypto.Cipher模块，ImportError: No module name 'Crypto'解决方案
请到官方网站:https://www.dlitz.net/software/pycrypto/ 下载pycrypto.
下载后，按照README中的"Installation"小节提示进行pycrypto安装
"""

class FormatException(Exception):
    pass

def throw_exception(message,exception_class=FormatException):
    """My define raise exception function"""
    raise exception_class(message)

class SHA1:
    """计算公众平台的消息清明接口"""

    def getSHA1(self,token,timestamp,nonce,encrypt):
        """用SHA1算法生成安全签名
        @:param token: 票据
        @:param timestamp: 时间戳
        @:param encrypt: 密文
        @:param nonce: 时间字符串
        @:return: 安全签名
        """
        try:
            sortlist = [token,timestamp,nonce,encrypt]
            sortlist.sort()
            sha = hashlib.sha1()
            sha.update("".join(sortlist))
            return WXBizMsgCrypt_OK,sha.hexdigest()
        except Exception:
            return WXBizMsgCrypt_ComputeSignature_Error,None

class XMLParse:
