import requests
import time
from lxml import etree
from selenium import webdriver

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'referer': 'https://manhua.fzdm.com/39/001/',
}
# URL = 'https://www.qcc.com/web/search?key=%E6%B9%96%E5%8D%97%20%E8%A1%A1%E9%98%B3%20%E8%92%B8%E6%B9%98%E5%8C%BA&filter=%7B%22ct%22%3A%5B%2270%22%5D%7D'

#chromedriver的地址，根据个人不同进行修改。
# Driver_path = r'C:/Program Files/Python3.9.1/Scripts/geckodriver.exe'
#设置ChromeOptions，实现不显示页面自动执行。
# Option = webdriver.FirefoxOptions()
# Option.add_argument('headless')
#导入设置，建立Driver。
# Driver = webdriver.Firefox(executable_path=Driver_path, options=Option)
# req = requests.get(url=URL, headers=HEADER)
#
# Driver.get(URL)
# modal = Driver.find_element_by_xpath('//ul[@class="navi-nav pull-right lpan"]/li[last()]')
# modal.click()



def gotoWork(keyword, code):
    keyword = keyword.replace('"', '')
    URL = "https://www.qcc.com/web/search?key=" + keyword + "&filter=%7B%22ct%22%3A%5B%2270%22%5D%7D"
    req = requests.get(url=URL, headers=HEADER)
    req.encoding = 'utf-8'
    html = etree.HTML(req.text)
    item = html.xpath("//table[@class='ntable ntable-list']/tr/td[3]/div/a")
    with open('success.csv', 'a', encoding='utf-8-sig') as f:
        for x in item:
            name = ''.join(x.xpath('.//span//text()'))
            print('"' + keyword + '" ' + '"' + name + '" "' + x.xpath('.//@href')[0]+'"' ) #+ "''.join(x.xpath('.//span//text()'))" + "x.xpath('.//@href')[0]"
            str = '"' + keyword + '",' + '"' + name + '",' + code + ',"' + x.xpath('.//@href')[0]+'"\n'
            f.write(str)
    f.close()
# gotoWork('无极县 石家庄市 河北省')

def readBook():
    with open('book.txt', 'r', encoding='UTF-8-SIG') as f1:
        list = f1.readlines()
        for i in range(0, len(list)):  #len(list)
            str = list[i].rstrip().split(',')
            gotoWork(str[5] + ' ' + str[3] + ' ' + str[1], str[0])
            time.sleep(2)
readBook()