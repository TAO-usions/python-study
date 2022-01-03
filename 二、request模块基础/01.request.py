# 爬虫搜狗首页的页面数据
import requests as re
if __name__ =="__main__":
    # 1.指定url
    url='https://www.sogou.com/'
    # 2. 发起请求
    # get方法回返回一个响应
    response=re.get(url=url)
    # 3、获取响应数据。text返回的是字符串形式的响应数据
    page_text=response.text
    print(page_text)
    # 4、持久化存储
    with open('./sougou.html','w',encoding="utf-8") as fp:
        fp.write(page_text)
        fp.close()

 