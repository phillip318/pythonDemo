# 第一部分目录页解析主要使用库：
import requests
from lxml import etree
# 第二部分详情页解析主要使用库：
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# 其他辅助库
import time
import os
import re

#要爬取的网页网址

URL= 'https://manhua.fzdm.com/39/'
# URL = 'https://www.vmgirls.com/'

# 建立用于伪装的header：包括User-Agent、referer和cookie。

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'referer': 'https://manhua.fzdm.com/39/001/',
}

#chromedriver的地址，根据个人不同进行修改。
Driver_path = r'C:/Program Files/Python3.9.1/Scripts/geckodriver.exe'
#设置ChromeOptions，实现不显示页面自动执行。
Option = webdriver.FirefoxOptions()
Option.add_argument('headless')
#导入设置，建立Driver。
Driver = webdriver.Firefox(executable_path=Driver_path, options=Option)

def parse_catalogue(url,id):
#调用requests库中的get命令，获取要爬取的目录页内容
    req = requests.get(url=url, headers=HEADER)
#通过lxml库中etree.HTML将解析字符串格式的HTML文档对象，注意：使用req.content获取的是网页的bytes型也就是二进制的数据。
    html = etree.HTML(req.content)
    href = html.xpath("//div[@id='content']/li/a/@href")
    href.reverse()
    if id in href:
        index = href.index(id,0)
        href = href[index:]
    #在我们得到了所有的href后，通过for循环将其取出，通过字符串的组合我们我们就能得到详情页的真是网址，即content_url。例：“https://manhua.fzdm.com/1/ + brc25/ ”
    for x in href:
        content_url = URL + x
    #打印组合完成的新网址，这样在爬取的时候，我们就可以看到下载到了哪里。
    #将content_url得到的网址传入到parse_content函数，这里使用的parse_content函数是下面要建立的详情页解析函数。
        parse_content(content_url)
    #使用time函数，每次解析一个网页后停滞2秒。
        time.sleep(1)



def parse_content(url):
    # 使用Driver.get打开详情页
    Driver.get(url)
    # 获取详情页中该回漫画的名称，find_element_by_xpath是使用xpath语法的形式进行定位，注意这里虽然定位的方式使用的是xpath，但是该方法是用来定位element的，不能直接获得text，所以需要在获取到的element最后使用“.text”方法获得其中文本内容。
    title = Driver.find_element_by_xpath('//div[@id="pjax-container"]/h1').text
    #使用os函数建立多层目录，我把目录建立都在e盘的comic文件夹下，按照漫画章节标题单独建立目录。
    if os.path.isdir(title):
        pass
    else:
        os.makedirs(title)
    print(title)
    # 因为在网页中，我们没有办法一目了然地看到该回漫画总计页数，所以在这里使用while True循环，让他不断遍历，直到达到相应的条件，则终止循环。
    while True:
        # 显式等待，每次进入新网页img标签出现再进行下一步
        WebDriverWait(Driver,10).until(ec.presence_of_element_located((By.XPATH,"//div[@id='mhimg0']//img")))
        # 获取每一个页面中，漫画图片的真实地址。
        img = Driver.find_element_by_xpath("//div[@id='mhimg0']//img")
        src = img.get_attribute("src")
        # 使用requests.get请求图片的网址
        comic_content = requests.get(url=src, headers=HEADER)

        # 将图片保存到对应文件夹中，文件名按照下载的图片名定义
        print('等待写入 ', re.search('\w+.jpg', src).group())
        with open(title + '/' + re.search('\w+.jpg', src).group(), 'wb') as f:
            f.write(comic_content.content)
            print('写入完成 ', re.search('\w+.jpg', src).group())

        # 等待a标签的出现。
        WebDriverWait(Driver, 10).until(ec.presence_of_element_located((By.ID, 'xuanfu_news_id')))
        a = Driver.find_element_by_xpath("//div[@id='xuanfu_news_id']/a[@href='javascript:void();']")
        a.click()

        #当该回漫画到最后一页，会在网页最后出现“最后一页了”的字样，在这里当出现最后一页了的字样后，循环停止跳出，否则只要出现“下一页”字样，就重复循环。
        end_story = ec.text_to_be_present_in_element((By.XPATH, '//div[@class="navigation"]'), '最后一页了')(Driver)
        if end_story is True:
            print('最后一页')
            break
        else:
            print('下一页')
            next_page = Driver.find_element_by_link_text('下一页')
            WebDriverWait(Driver,10).until(
                ec.presence_of_element_located((By.XPATH,'//a[@class="pure-button pure-button-primary"]'))
            )
            next_page.click()

parse_catalogue(URL,'48/')