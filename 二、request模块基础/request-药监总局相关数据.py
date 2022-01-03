
import requests
if __name__ == "__main__":
    url='http：//125.35.6.84:81/xk'
    headers = {
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

    }
    response = requests.get(url=url ,headers=headers).text

    with open('./huazhuangpin.html','w',encoding="utf-8") as fp:
        fp.write(response)

        