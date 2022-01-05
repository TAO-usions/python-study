import json
import requests
if __name__ == "__main__":
    url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

    }
    data = {
        'on':'true',
        'page':'1',
        'pageSize':'15','productName':'','conditionType':'1','applyname':'','applysn':'',

    }
    id_list = [] #存储企业的id
  
    json_ids= requests.get(url=url ,headers=headers).text
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(id_list)
    # with open('./huazhuangpin.html','w',encoding="utf-8") as fp:
    #     fp.write(response)

        