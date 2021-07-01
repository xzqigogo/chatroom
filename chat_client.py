#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : chat_client.py
@Author: Piepis
@Date  : 2021/6/30 下午6:47
@Desc  : 
夏泽祺的程序
'''
from socket import *

class Client_serve(object):
    def __init__(self, ADDR, HOST):
        self.ADDR = ADDR
        self.HOST = HOST
        self.ADDRESS = (self.ADDR, self.HOST)
        self.sockfd=socket(AF_INET,SOCK_STREAM)
        self.sockfd.connect(ADDR)
        self.main()

    def main(self):
        print("*********************************")
        print("*******请输入你要做的操作************")
        print("*******1.创建用户******************")
        print("*******2.进入聊天室*****************")
        print("**********************************")