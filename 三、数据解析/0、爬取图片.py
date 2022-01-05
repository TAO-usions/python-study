

import requests

if __name__ == "__main__":
    url="https://baike.baidu.com/pic/%E6%98%9F%E6%B8%B8%E8%AE%B0/24123/1646254386/77c6a7efce1b9d16905d8e9ef3deb48f8d5464b2?fr=newalbum#aid=1646254386&pic=77c6a7efce1b9d16905d8e9ef3deb48f8d5464b2"
    img_data = requests.get(url=url).content
    #text(字符串) content（二进制） json（）（对象）

    with open('./qiutu.jsp','wb') as fp:
        fp.write(img_data)