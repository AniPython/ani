"""
使用 requests 和 re
$ pip install requests
"""
import requests
import re

response = requests.get("http://anipython.com/crawler/1/")
html_text = response.text
result = re.findall(r'<div class="card-body">(.*?)</div>', html_text, re.S)[0].strip()
print(result)
# 输出: Hello world
