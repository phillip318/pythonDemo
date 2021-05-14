# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

'''
word = '字符串'
sentene = '这是一个句子'
paragraph = """
    这是一个段落
    可以由多行组成
"""
print(word)
print(sentene)
print(paragraph)

'''

'''
# 单引 和双引 区别
# my_str = "I' a student"
my_str = "I\' a student"
print(my_str)
'''

str = "hengyang"
print(str[3])
print(str[1:2]) # 输出 第一个下标到第二个下标，但不包括第二个下标
print(str[:4])
print(str[4:])

print(r"hello\nhengyang")  #r 不解释转移字符