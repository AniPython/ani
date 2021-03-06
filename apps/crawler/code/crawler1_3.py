"""
使用 requests 和 xpath
$ pip install requests
$ pip install lxml
如果安装出错可以尝试更换国内源
$ pip install -i https://pypi.doubanio.com/simple lxml
"""
import requests
from lxml import etree

response = requests.get("http://anipython.com/crawler/1/")
html_text = response.text
html_element = etree.HTML(html_text)
result = html_element.xpath('//div[@class="card-body"]/text()')[0].strip()
print(result)
# 输出: Hello world
