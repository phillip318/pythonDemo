# -*- codeing = utf-8 -*-
# @Time : 2021/1/25 0025 14:56
# @Author: 罗路
# @File: girls-home.py
# @Software: PyCharm
import time

import requests
import re
import os

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
response = requests.get("https://www.vmgirls.com/", headers=headers)
html = response.text

urls = re.findall('<a class=media-content href=(.*?) .*?>',html)
print(urls)
# urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)