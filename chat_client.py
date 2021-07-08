#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : chat_client.py
@Author: Piepis
@Date  : 2021/6/30 下午6:47
@Desc  : 
夏泽祺的程序
'''
import time
from socket import *
import pymysql
import re


class Client_serve(object):
    def __init__(self, ADDR, HOST):
        self.ADDR = ADDR
        self.HOST = HOST
        self.ADDRESS = ((self.ADDR, self.HOST))
        self.sockfd = socket(AF_INET, SOCK_STREAM)
        self.sockfd.connect(self.ADDRESS)
        self.main()

    def chat_start(self):


    def main(self):
        while True:
            print("*********************************")
            print("*******请输入你要做的操作************")
            print("*******1.创建用户******************")
            print("*******2.进入聊天室*****************")
            print("**********************************")
            try:
                option = int(input("请输入你要操作的选项"))
            except Exception as e:
                print('输入信息有误请重新输入')
                continue
            else:
                if option not in (1, 2):
                    print('输入信息有误请重新输入')
                    continue
                elif option == 1:
                    while True:
                        name = input("请输入你要创建的账号名称")
                        if len(name) > 10:
                            print("账号名称无法超过10个字符")
                            continue
                        while True:
                            password = input("请输入密码")
                            # print(re.findall('\w{6,15}', password))  #测试语句
                            if re.findall('\w{6,15}', password)[0] != password:
                                print("密码只能是大于6小于12的字母或者数字")
                                continue
                            break
                        sqlword = 'insert into user_infor values("%s","%s")' % (name, password)
                        self.sockfd.send(("L " + sqlword).encode())
                        print("注册中，请稍等")
                        data01 = self.sockfd.recv(128).decode()
                        if data01 == 'ok':
                            print("创建用户成功")
                            break
                        else:
                            print("错误，请重新操作")
                            break
                else:
                    while True:
                        name = input('请输入用户账号:')
                        password = input('请输入密码:')
                        sqlword = 'select * from user_infor where name="%s"' % name
                        self.sockfd.send(('I ' + sqlword).encode())
                        time.sleep(0.1)
                        data = self.sockfd.recv(128).decode()  # data是判断用户名是否存在的指标
                        if data == 'no':
                            print("用户名不存在")
                            continue
                        else:
                            self.sockfd.send(password.encode())
                            data = self.sockfd.recv(1024).decode()
                            if data == 'ok':
                                print('登录成功')
                                self.chat_start()
                            else:
                                print("密码错误，请重新登录")
                                continue


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8888
    c01 = Client_serve(host, port)
