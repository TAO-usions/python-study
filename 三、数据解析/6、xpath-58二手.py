

from lxml import etree
import requests as re

if __name__ == "__main__":
    headers = {
       'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    #爬取到页面源码数据
    url='https://bj.58.com/ershoufang/'
    page_text=re.get(url=url,headers=headers).text

    #数据解析
    tree=etree.HTML(page_text)
    #存储的就是li标签对象
    li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp=open('58.txt','w',encoding="utf-8")
    for li in li_list:
        #局部解析
        title=li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')