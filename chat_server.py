#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : chat_server.py
@Author: Piepis
@Date  : 2021/6/30 下午6:46
@Desc  : 
夏泽祺的程序
'''
import sys
from socket import *
import os

# 地址及端口号设置
ADDR = '127.0.0.1'
HOST = 8888
ADDRESS = (ADDR, HOST)


# 用类封装所有服务端功能

class Chat_Serve(object):
    def __init__(self, ADDR, HOST):
        self.ADDR = ADDR
        self.HOST = HOST
        self.ADDRESS = (self.ADDR, self.HOST)
        self.link_sockfd()
        self.main()

    def link_sockfd(self):
        self.sockfd = socket(AF_INET, SOCK_STREAM, proto=0)
        self.sockfd.bind(self.ADDRESS)
        self.sockfd.listen(5)

    def manage(self):
        pass

    def connect_inter(self):
        connfd, addr = self.sockfd.accept()
        judge = connfd.recv(128).decode()#judge为判断用户输入的操作要求
        if judge=="L "

    def main(self):
        pid = os.fork()
        if pid < 0:
            sys.exit('end system....')
        elif pid == 0:
            self.manage()
        else:
            self.connect_inter()
