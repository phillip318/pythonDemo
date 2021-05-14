# -*- codeing = utf-8 -*-
# @Time : 2021/1/22 0022 10:52
# @Author: 罗路
# @File: spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup   #网页解析 ，获取数据
import re     #正则
import urllib.request,urllib.error   #指定网页url，获取数据
import xlwt        #操作excel
import sqlite3    #操作sqlite数据库

def main():
    baseUrl = "https://movie.douban.com/top250?start=0"
    #1. 爬取网页
    datalist = getData(baseUrl)

    #3. 保存数据
    savepath = "豆瓣电影Top250.xls"
    saveData(datalist, savepath)


#影片链接
findLink = re.compile(r'<a href="(\S+)">')
#影片封面
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  # re.S  让换行符包含在字符中，一般情况下.  是不包含的
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


def getData(baseUrl):
    datalist = []
    for i in range(0,10):   #调用获取页面信息的函数
        url = baseUrl + str(i*25)
        html = askURL(url)

        #2 逐一解析
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink,item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')   #外语名称留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","") #去掉句号
                data.append(inq)
            else:
                data.append(' ')  #留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('(\s+)?', '', bd)
            bd = re.sub('<br/>','',bd)
            bd = re.sub('/','',bd)  #替换 /

            data.append(bd.strip())  #去掉前后空格


            datalist.append(data)
    return datalist

#得到一个指定网页信息的方法
def askURL(url):
    #模拟头部信息
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#3. 保存数据
def saveData(datalist,savepath):
    print('save...')
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 是否压缩
    sheet = book.add_sheet(savepath,cell_overwrite_ok=True)  # 覆盖以前的内容
    col = ("电影详情","封面","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)
    print('保存完毕')

if __name__ == "__main__":   #当程序执行main方法时
    #调用函数
    main()

