# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

# 捕获异常
'''
try:
    f = open('test2.txt','r')
    print(num)
except Exception as result:
    print('产生异常了')
    print(result)
'''

import time

try:
    f = open('123.txt','r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print('发生异常')
    print(result)
