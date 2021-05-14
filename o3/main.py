import requests
import time
from lxml import etree
# 第二部分详情页解析主要使用库：
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os


#chromedriver的地址，根据个人不同进行修改。
Driver_path = r'C:/Program Files/Python3.9.1/Scripts/geckodriver.exe'
#设置ChromeOptions，实现不显示页面自动执行。
Option = webdriver.FirefoxOptions()
Option.add_argument('headless')
Driver = webdriver.Firefox(executable_path=Driver_path, options=Option)
from lxml.html import fromstring, tostring
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'referer': 'https://manhua.fzdm.com/39/001/',
}


def reqHuobiGlobal(bitName):
    URL = "https://www.huobi.de.com/zh-cn/exchange/"
    flag = False;
    # 使用Driver.get打开详情页
    Driver.get(URL)
    time.sleep(4)
    # 获取详情页中该回漫画的名称，find_element_by_xpath是使用xpath语法的形式进行定位，注意这里虽然定位的方式使用的是xpath，但是该方法是用来定位element的，不能直接获得text，所以需要在获取到的element最后使用“.text”方法获得其中文本内容。
    list = Driver.find_elements_by_xpath("//div[@class='vue-recycle-scroller__item-view']")

    for i in list:
        name = i.find_element_by_xpath('.//em').text
        if (name == bitName) :
            flag = True
    if(flag == False):
        time.sleep(4)
        Driver.refresh()
        reqHuobiGlobal(bitName)
    else:
        os.system('龙的传人.mp3')
        print('发现' + bitName)

reqHuobiGlobal('XCH')