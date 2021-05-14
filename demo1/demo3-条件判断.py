# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

# password = input('请输入密码：')
# print('您刚刚输入的密码是：%s'%password)

# a = 10
# a = 'abc'
# print(type(a))    input输入的内容 全都是string类型

'''
a = int("123")
b = a + 100
print(b)

c =  int(input('输入c:'))
print('输入了一个数字%d'%c)
'''


if True:               # 0 为false
    print('Ture')
else:
    print('False')
print('end')     # 如果接缩进就会进else， 如果和if  同缩进 则是平级


score = 87
if score >=90 and score<=100:
    print('本次考试，等级未A')
elif score<90:
    print('本次考试，等级为B')

import random #引入随机库

x = random.randint(0,2)   #包含 0,1,2  三个随机数
print(x)