"""
安装依赖:
$ pip install pandas
$ pip install openpyxl

思路:
先访问第一页
然后不断点击下一页
直到下一页不可点击为止
"""

import requests
from lxml import etree
import pandas as pd

host = 'http://127.0.0.1:8000'
base_url = f"{host}/crawler/4/?page="
p = 1  # 从第一页开始, 每循环一个次 p 自增 1
is_break = False  # 控制 while True 循环跳出
all_title_url_list = []


def get_current_title_url_list(url) -> list:
    """
    获取单个页面下的全部 title url
    :param url: url 地址
    :return: title 的 href 属性的多个值组成的列表
    """
    global is_break
    response = requests.get(url)
    text = response.text
    element = etree.HTML(text)

    # 不断获取下一页的url, 直到 li 标签出现 class="disabled"
    if "disabled" in element.xpath('//ul[@class="pagination"]/li[last()]/@class')[0]:
        is_break = True

    return element.xpath('//div[@class="title"]/p/a/@href')


def get_all_title_url_list():
    """
    获取所有的 title_url
    :return: list
    """
    global p, all_title_url_list
    while True:
        title_url_list = get_current_title_url_list(base_url + str(p))
        all_title_url_list.extend(title_url_list)
        p += 1
        if is_break:
            break


def get_detail(url):
    """
    解析详情页
    """
    response = requests.get(url)
    text = response.text
    element = etree.HTML(text)

    # 开始解析每个字段的值
    title = element.xpath('//div[@class="card-body"]//h4[@class="title"]/a/text()')[0]
    url = element.xpath('//div[@class="card-body"]//h4[@class="title"]/a/@href')[0]
    desc = element.xpath('//div[@class="card-body"]//p/text()')[0]

    # 组成列表直接返回
    return [title, url, desc]


if __name__ == '__main__':
    # 1: 获取全部的 title url
    get_all_title_url_list()

    # 2: 遍历全部的 title url, 获取详情
    result_2d_list = []
    for title_url in all_title_url_list:
        result_2d_list.append(get_detail(host + title_url))

    # 3: 遍历全部的 title url, 获取详情
    df = pd.DataFrame(result_2d_list, columns=["title", "url", "desc"])
    df.to_excel('results.xlsx', index=False)