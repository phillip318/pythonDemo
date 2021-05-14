# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

#增加：  append
'''

namelist = ['小张','小王','小李']

print('---增加前，名单列表的数据---')
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名:")
namelist.append(nametemp)  #在末尾追加元素   类似Push

print('---增加后，名单列表的数据---')
for name in namelist:
    print(name)
'''




'''
a = [1,2]
b = [3,4]
# a.append(b)
# print(a)

a.extend(b)  #将b 逐个追加到a列表种
print(a)
'''

'''
#增
a = [0,1,2]
a.insert(1,3)  # 指定下标 增加指定元素
print(a)
'''

'''
#删
moviename = ['骇客帝国','金钱帝国','速度与激情']
print(moviename)
del moviename[1]

moviename.remove('骇客帝国')  # 删除找到的第一个  骇客帝国
# moviename.pop()  删除最后一个
print(moviename)
'''

'''
#改
moviename = ['骇客帝国','金钱帝国','速度与激情']
moviename[1] = '我是杀人犯'
print(moviename)
'''

'''
#查询    in , not in
moviename = ['骇客帝国','金钱帝国','速度与激情']

findName = input("请输入你要查找的电影名称：")
if findName in moviename:
    print("在列表中找到了")
else:
    print('没找到')

'''

'''
# index方法  查找元素，从哪到哪
mylist = ['a','b','c','d','e']
print(mylist.index('c',0,4))

print(mylist.count('d'))  #统计d出现了几次
'''

'''
a = [1,2,3,4]
a.reverse()
print(a)
a.sort()
print(a) 
'''

offices = [[],[],[]]
schoolName = [['北京大学','清华大学'],['南开大学','天津大学'],['山东大学']]
print(schoolName[0][0:])

import random
names = ['A','B','C','D','E']
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

print(offices)