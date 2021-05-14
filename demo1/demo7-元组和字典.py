# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

'''
tup1 = () #创建空的元组

print(type(tup1))

tup2 = (50,)  # 元组 只有一个元素时  需要追加逗号

print(type(tup2))
'''

# tup1 = ('abc',123)
# print(tup1[1])


#增
'''
tup1 = (12,34,56)
# tup1[0] = 100  #元组不可修改元素
tup2 = ('xyz',)
tup = tup1 + tup2
print(tup)
'''

#删
'''
tup1 = (12,34,56)
del tup1
print(tup1)  #删除变量    而不是清空
'''

#字典
'''
info = {"name": "吴彦祖", "age": 18}
print(info['name'])
# print(info['name1']) #直接访问会报错
# print(info.get('name1'))   # 未找到 返回none
print(info.get('name1','m'))  #没找到 用m替代默认值
'''

info = {"name": "吴彦祖", "age": 18}
# newId = input("请输入学号：")
# info["id"] = newId

# del info["name"]  #删除了键， 不止是值  键值对都没了
# info.clear() # 清空整个字典
# print(info)
# print(info.keys())
# print(info.values())
# print(info.items())
#
# for key in info.keys():
#     print(key)
#
# for key in info.values():
#     print(key)
#
#
# for key,value in info.items():
#     print("key=%s,value=%s"%(key,value))

#enumerate 同时拿到内容 和下标
mylist = ['a','b','c','d']
for i,x in enumerate(mylist):
    print(i,x)


'''
列表
元组
字典
集合
'''