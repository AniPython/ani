"""
使用 urllib 和 re
"""
from urllib import request
import re


response = request.urlopen("http://anipython.com/crawler/1/")
html_text = response.read().decode('utf-8')
result = re.findall(r'<div class="card-body">(.*?)</div>', html_text, re.S)[0].strip()
print(result)
# 输出: Hello world