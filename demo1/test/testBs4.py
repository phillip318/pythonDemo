# -*- codeing = utf-8 -*-
# @Time : 2021/1/22 0022 11:51
# @Author: 罗路
# @File: testBs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup

file = open('./temp.html','rb')

html = file.read()
bs = BeautifulSoup(html,"html.parser")

# 获取的是标签节点对象
# print(bs.title)
# print(bs.a)
# print(type(bs.head))

# print(type(bs.title.string))
# print(bs.meta.attrs["charset"])
# print(bs.a.string)
# print(type(bs.a.string)) #comment 注释

# print(bs.head.contents[1])

# t_list = bs.find_all("a")
import re
# t_list = bs.find_all(re.compile('m'))
# print(t_list)

#方法 ???
'''
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)

for item in t_list:
    print(item)
'''
# t_list = bs.find_all(id="news")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(text=["新闻","动漫"])
# t_list = bs.find_all(text=re.compile("\d"))
# t_list = bs.find_all(text=re.compile("\d"), limit=2)
# print(t_list)


#css选择器  select 可根据 标签 id 类名
# print(bs.select("title"))
# print(bs.select("head title"))
# print(bs.select(".tiyu ~ .xinwen")[0].string)
# print(bs.select(".tiyu ~ .xinwen")[0].get_text())
bs = str(bs)
print(re.findall('<p class="">(.*?)</p>',bs,re.S))


