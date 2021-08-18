import requests
from lxml import etree


host = 'http://127.0.0.1:8000'
profile_url = f"{host}/user/profile/"

# 下面设置的 sessionid 以你自己实际获取的为准
headers = {
    "Cookie": "sessionid=e6esf37mby4a20zgp15xyf6rz050a43h"
}

# headers -> Cookie -> sessionid
# dajngo 后端通过 sessionid 检验用户
response = requests.get(url=profile_url, headers=headers)
element = etree.HTML(response.text)
result = element.xpath('//div[@class="container"]//text()')
print(result)
# 输出: ['\n    ', '个人中心', '\n    ', '你的用户名是:&nbsp', 'ani', '\n']
