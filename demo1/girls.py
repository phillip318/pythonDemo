# -*- codeing = utf-8 -*-
# @Time : 2021/1/22 0022 17:46
# @Author: 罗路
# @File: girls.py
# @Software: PyCharm




"""请求网页"""
import time

import requests
import re
import os
import urllib.request,urllib.error

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
homePath = 'https://www.vmgirls.com/'

response = requests.get(homePath, headers=headers)
html = response.text
urls = re.findall('<a class=media-content href=(.*?) .*?>',html)

for item in urls:
    res = requests.get(homePath + item, headers=headers)
    Html = res.text
    # Urls = re.findall('<a .*?><img .*?data-pagespeed-lsc-url="(.*?)"/></a>', Html)
    Urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', Html)
    dir_name = re.findall('<h1 class="post-title h1">(.*?)</h1>', Html)[-1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    for i in Urls:
        time.sleep(0.5)
        url = i.replace('//', 'https://')
        result = requests.get(url, headers=headers)
        print(dir_name + '/' + i.split('/')[-1])
        with open(dir_name + '/' + i.split('/')[-1], 'wb') as f:
            f.write(result.content)
'''解析网页
dir_name = re.findall('<h1 class="post-title h1">(.*?)</h1>',Html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)


urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',Html)
for i in range(0,len(urls)):
    time.sleep(1)

    url = urls[i].replace('//','https://')
    response = requests.get(url,headers=headers)
    with open(dir_name +'/' + file_name,'wb') as f:
        f.write(response.content)
'''