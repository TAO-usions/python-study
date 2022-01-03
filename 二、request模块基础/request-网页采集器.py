# UA伪装：
#UA：User-Agent（请求载体的身份标识）
# UA检测：门户网站的服务器会对检测对应请求的载体身份标识，如果检测到请求载体的身份标识为某一款浏览器的
# 说明该请求是一个正常的请求，但，如果检测到请求不是一款浏览器，则表示该请求是为不正常的请求（爬虫）

# UA伪装：让爬虫对应的请求载体身份标识伪装成一款浏览器
import  requests as re

if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    url='https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw=input('enter a word')
    param = {
        'query':kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理参数
    response=re.get(url=url,params=param,headers=headers)

    page_text=response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding="utf-8" ) as fp:
        fp.write(page_text)
    print(fileName,"保存成功")