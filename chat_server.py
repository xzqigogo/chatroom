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
import time
from socket import *
import os
import pymysql

# 地址及端口号设置
ADDR = '127.0.0.1'
HOST = 8888
ADDRESS = (ADDR, HOST)


# 用类封装所有服务端功能

class Chat_Serve(object):
    def __init__(self, ADDR, HOST):
        self.ADDR = ADDR
        self.HOST = HOST
        self.ADDRESS = ((self.ADDR, self.HOST))
        self.log=[]
        self.link_sockfd()
        self.main()

    def link_sockfd(self):
        self.sockfd = socket(AF_INET, SOCK_STREAM, proto=0)
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        self.sockfd.bind(self.ADDRESS)
        self.sockfd.listen(5)

    def connect_mysql(self, sql_language=None):
        # connect database
        db = pymysql.connect(user='root', password='123456',
                             host='127.0.0.1', port=3306, database='chatroom', charset='utf8')
        cur = db.cursor()
        cur.execute(sql_language)
        fetchone = cur.fetchall()
        time.sleep(0.2)
        db.commit()
        cur.close()
        db.close()
        if not fetchone:
            return
        else:
            return fetchone

    def chat_start(self):
        pass


    def manage(self):
        pass

    def connect_inter(self):
        self.connfd, addr = self.sockfd.accept()
        self.log.append(self.connfd)
        while True:
            judge = self.connfd.recv(128).decode()  # judge为判断用户输入的操作要求
            judgelist = judge.split(' ')
            if judgelist[0] == "L":
                print(' '.join(judgelist[1:]))  # 测试print
                self.connect_mysql(' '.join(judgelist[1:]))
                self.connfd.send(b'ok')
            elif judgelist[0] == "I":
                print(' '.join(judgelist[1:]))
                user_info=self.connect_mysql(' '.join(judgelist[1:]))
                # print(user_info)#测试语句，测试user_info的值
                if not user_info:
                    self.connfd.send(b'no')
                else:
                    self.connfd.send(b'ok')
                    input_password=self.connfd.recv(1024).decode()
                    print(input_password)
                    if input_password==user_info[0][1]:
                        self.connfd.send(b'ok')
                        self.chat_start()
                    else:
                        self.connfd.send(b'wrong')

    def main(self):
        pid = os.fork()
        if pid < 0:
            sys.exit('end system....')
        elif pid == 0:
            # print('进程1开始操作咯')
            self.manage()

        else:
            # print('进程2开始操作咯')
            self.connect_inter()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8888
    c01 = Chat_Serve(host, port)
