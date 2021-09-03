"""
爬取图片
"""

# 1: 获取图片地址
import requests
from lxml import etree

host = 'http://anipython.com'

response = requests.get(f"{host}/crawler/5/")
text = response.text
element = etree.HTML(text)

img_src = element.xpath('//div[@class="card-body"]//img/@src')[0]
img_url = host + img_src


# 2: 下载图片
# 2.1: 方法一, 使用内置的 urllib
from urllib.request import urlretrieve
urlretrieve(img_url, 'urlretrieve.png')

# 2.2: 方法二, 使用第三方库 requests
img_data = requests.get(img_url).content
with open('requests.png', 'wb') as fp:
    fp.write(img_data)
