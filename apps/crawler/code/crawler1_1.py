"""
使用 urllib 和 re
"""
from urllib import request
import re

host = 'http://127.0.0.1:8000'
response = request.urlopen(f"{host}/crawler/1/")
html_text = response.read().decode('utf-8')
result = re.findall(r'<div class="card-body">(.*?)</div>', html_text, re.S)[0].strip()
print(result)
# 输出: Hello world