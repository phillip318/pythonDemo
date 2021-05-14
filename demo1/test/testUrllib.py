# -*- codeing = utf-8 -*-
# @Time : 2021/1/22 0022 11:12
# @Author: 罗路
# @File: testUrllib.py
# @Software: PyCharm

import urllib.request

#获取一个get请求地址
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))   #对获取到的网页源码进行 utf-8解码


#获取一个post请求地址
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"name":"luolu"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))


# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out")

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Cache-Control"))


# import urllib.parse
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name":"luolu"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
#
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


url = "http://douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))