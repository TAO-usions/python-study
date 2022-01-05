import requests as re
from lxml import etree
import os
if __name__ == "__main__":
    headers = {
         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    url = 'http://pic.netbian.com/4kmeinv'
    # page_text=re.get(url=url,headers=headers).text
    response = re.get(url=url,headers=headers)
    #手动设定响应数据的编码格式
    # response.encoding='utf-8'
    page_text=response.text
    #数据解析：src的属性值 alt属性
    tree=etree.HTML(page_text)

    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    
    #创建一个文件夹
    if not os.path.exists('./icLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        img_src='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        # 通用处理中文乱码的解决方案
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name,img_src)
        #请求图片进行持久化存储
        img_data=re.get(url=img_src,headers=headers)
        img_path='picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data.content)
            print(img_name,'下载成功')