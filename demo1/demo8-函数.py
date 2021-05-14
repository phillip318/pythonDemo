# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

'''

def printinfo():
    print('---------------------------------')
    print(' 人生苦短，我用Python  ')
    print('---------------------------------')

#函数调用
printinfo()
'''

'''
#带参函数
def add2Num(a,b):
    c = a + b
    print(c)

add2Num(11,22)
'''

'''
#带返回值
def add2Num(a,b):
    return  a + b

print(add2Num(11,22))
'''

#返回多个值
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu

sh,yu = divid(5,2)

print("商:%d, 余数:%d"%(sh,yu))