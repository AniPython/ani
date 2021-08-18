"""
使用 requests 和 re
$ pip install requests
"""
import requests
import re

host = 'http://127.0.0.1:8000'
response = requests.get(f"{host}/crawler/1/")
html_text = response.text
result = re.findall(r'<div class="card-body">(.*?)</div>', html_text, re.S)[0].strip()
print(result)
# 输出: Hello world