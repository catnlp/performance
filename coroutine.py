# -*- coding: utf-8 -*-
# @Author  : catnlp
# @FileName: coroutine.py
# @Time    : 2020/9/5 10:51


def customer():
    while True:
        number = yield
        print('开始消费：', number)


custom = customer()
next(custom)
for i in range(10):
    print('开始生产：', i)
    custom.send(i)
