import requests
from lxml import etree

profile_url = "https://anipython.com/user/profile/"

# 下面设置的 sessionid 以你自己实际获取的为准
headers = {
    "Cookie": "sessionid=f11pwkldxclkjx3kt5tzixl4uyf5d3y2"
}

# headers -> Cookie -> sessionid
# dajngo 后端通过 sessionid 检验用户
response = requests.get(url=profile_url, headers=headers)
element = etree.HTML(response.text)
result = element.xpath('//h3//text()')
print(result)
# 输出: ['AniPython', '\xa0的个人中心']
