# -- coding: utf-8 --
import os
import requests
from bs4 import BeautifulSoup

#设置当前文件为python工作路径，否则默认工作路径为I:/Python，导致所有命令无法执行
#os.chdir(os.path.dirname(__file__))


# 设置爬虫的headers，否则被认为是机器人
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}

#爬取的网址
wangzhis = [
    'https://search.smzdm.com/?c=faxian&s=洗碗机+10套&order=time&max_price=2000&v=b',
    'https://search.smzdm.com/?c=faxian&s=电视+65寸&order=time&max_price=1500&v=b',
    'https://search.smzdm.com/?c=faxian&s=电视+55寸&order=time&max_price=1300&v=b',
    'https://search.smzdm.com/?c=faxian&s=交换机+千兆&order=time&max_price=35&v=b',
    'https://search.smzdm.com/?c=faxian&s=wifi6&order=time&max_price=200&v=b',
 #   'https://search.smzdm.com/?c=faxian&s=对开门冰箱&order=time&max_price=2100&v=b',
#    'https://search.smzdm.com/?c=faxian&s=显示器+24&order=time&max_price=450&v=b',
    
]

# print(stocks)
# os._exit(0)
wenZi =[]
#获取文本上的内容，每一行，可以直接用wenZi[i]来获取
with open('smzdm.txt', mode='r+', encoding='utf-8') as f:
    wenZi = f.readlines()

# 开始每个股票代码爬取数据
for i in range(len(wangzhis)):
    #爬取网页
    print(str(i)+"====="+wangzhis[i])
    res1 = requests.get(wangzhis[i], headers=headers)
    #解析网页
    soup1 = BeautifulSoup(res1.text, "html.parser")

    #获取最新商品的标题
    tmpData = soup1.find('h5', {
        "class": "feed-block-title"
    }).get_text().strip()
    #将获取的信息合并成一行
    tmpData = "".join(tmpData.split())

    if wenZi[i].strip() != tmpData:
                wenZi[i] = tmpData
                # print(i)
                # print(wenZi[i])
                title = tmpData
                #推送微信，自行关注 “爱语飞飞”微信公众号获取自己的ID
                wx = requests.get('http://iyuu.cn/IYUU6390T1a631446bf43eacc9b344b63a63b12cebbf70679.send',params={'text':title,'desp':wangzhis[i]})
                print("有内容更新，成功发送")
            
    # if i == len(wangzhis)-1 :

#将新的写入text中
with open('smzdm.txt', mode='w', encoding='utf-8') as g:
        ceshi =  ''
        for j in range(len(wangzhis)):
            print(wenZi[j].strip())
            # print(j)
            ceshi =  ceshi + wenZi[j].strip() + '\n'
        # print(ceshi.strip())
        g.writelines(ceshi.strip())

            

os._exit(0)

