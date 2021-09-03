import requests
from lxml import etree

profile_url = "http://anipython.com/user/profile/"

# 下面设置的 sessionid 以你自己实际获取的为准
headers = {
    "Cookie": "sessionid=6ib8kwd1vy1sozmgvydwls53c6a5e1q1"
}

# headers -> Cookie -> sessionid
# dajngo 后端通过 sessionid 检验用户
response = requests.get(url=profile_url, headers=headers)
element = etree.HTML(response.text)
result = element.xpath('//div[@class="container"]//text()')
print(result)
# 输出: ['\n    ', '个人中心', '\n    ', '你的用户名是:&nbsp', 'ani', '\n']
