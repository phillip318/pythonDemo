# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

'''
f = open('test.txt','w') #w write  不存在创建 写入一个文件
f.write("hello world, i am here!") # 写入字符串
f.close()  #关闭文件
'''


'''

f = open('test.txt','r')
content = f.read(5)
print(content)
content = f.read(5)
print(content)
f.close()
'''


'''
#根据 行数来读取, 所有行  返回数组
f = open('test.txt','r')
content = f.readlines()
print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1
f.close()
'''

import  os
os.rename('test1.txt', 'test2.txt')