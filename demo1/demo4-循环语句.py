# -*- codeing = utf-8 -*-
# @Time : 2021/1/21 0021 14:42
# @Author: 罗路
# @File: demo1.py
# @Software: PyCharm

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,11,3):   #从0开始，到11结束，每次加3
    print(i)
'''

'''
for i in range(-10,-100,-30):
    print(i)
'''

'''
name = 'hengyang'
for x in name:
    print(x,end='')
'''

'''
a = ['aa','bb','cc']
for i in range(len(a)):
    print(i,a[i])

'''

'''
i = 0
while i < 5:
    print('当前是第%d次循环'%(i+1))
    i += 1
'''

'''
sum = 0
i = 0
while i<101:
    sum += i
    i += 1

print(sum)

count = 0
for x in range(1,101):
    count += x
print(count)
'''

'''       
i = 0
while i<10:
    i = i + 1
    print('-'*30)
    if i == 5:
        break
    print(i)
'''

# break 结束整个循环,   continue结束本次循环
i = 0
while i<10:
    i = i + 1
    print('-'*30)
    if i == 5:
        continue
    print(i)