
import json
import requests as re
if __name__ == "__main__":
    url='https://movie.douban.com/j/chart/top_list'
    params = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'60',  #从库中的第几部电影去取
        'limit':'20',   #一次取多少个
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

    }
    response = re.get(url, params=params, headers=headers)

    list_data=response.json()
    fp=open('./douban.json','w',encoding="utf-8")
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print("over!!")