

import requests as re
import json
if __name__ == "__main__":
    # 1、指定url
    post_url="https://fanyi.baidu.com/sug"
    # 2、进行UA伪装
    headers = {
        'User_Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

    }
    # 3、post请求参数处理（同get请求一致）
    word=input('enter a world')
    data={
        'kw':word
    }
    # data = {
    #     'kw':'dog'
    # }
    # 4、请求发送
    response=re.post(url=post_url,data=data,headers=headers)
    # 5、获取响应数据：json() 方法返回的是obj（如果确认响应数据是json数据类型的，才能使用json）
    # 从响应头Content-Type可知
    dic_obj=response.json()

    # 6、进行持久化存储
    fileName = word+'.json'
    fp=open(fileName,'w',encoding="utf-8")
    # fp=open('./dog.json','w',encoding="utf-8")
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print("over!!")