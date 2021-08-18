"""
直接找url的规律
<host>/crawler/3/?page=1 == <host>/crawler/3/
<host>/crawler/3/?page=2
<host>/crawler/3/?page=3
获取最大页码进行遍历
"""
import requests
from lxml import etree
import time

host = 'http://127.0.0.1:8000'

# 后端限制每秒最多访问 2 次, 平均每次是 0.5 秒, 所以每次请求之后 sleep 0.6 秒
sleep_time = 0.6

# 1. 发送请求, 获取最大页码
response = requests.get(f"{host}/crawler/3/")
time.sleep(sleep_time)
html_text = response.text
html_element = etree.HTML(html_text)
max_page = html_element.xpath('//li[contains(@class,"page-item")]/a[@class="page-link"]/text()')[-1]
# 得到的 max_page 是字符串类型的 "3"


# 2. 定义解析每一个页面的函数, 参数是页码
def parse_page(p):
    url = f"{host}/crawler/3/?page={p}"
    res = requests.get(url)
    time.sleep(sleep_time)
    text = res.text
    element = etree.HTML(text)
    result_list = element.xpath('//div[@class="poem"]//text()')
    result_list = [x.strip() for x in result_list if x.strip()]
    print(result_list)


# 3. 遍历每一页
for page in range(int(max_page)):
    parse_page(page + 1)
"""
输出:
['相思', '王维', '红豆生南国，', '春来发几枝。', '愿君多采撷，', '此物最相思。']
['鹿柴', '王维', '空山不见人，', '但闻人语响。', '返景入深林，', '复照青苔上。']
['渭城曲 / 送元二使安西', '王维', '渭城朝雨浥轻尘，', '客舍青青柳色新。', '劝君更尽一杯酒，', '西出阳关无故人。']
"""
