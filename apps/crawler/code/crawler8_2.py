from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

host = 'http://127.0.0.1:8000'
url = f'{host}/crawler/8/'

# 打开 Chrome 浏览器
driver = webdriver.Chrome()

# 等待, 最多等待5秒
wait = WebDriverWait(driver, 5)

# 这时跟方案一不同, 访问的是原始的页面的 url
# 方案一使用的 url 是 api 的url
driver.get(url)

# 对动态页面, 必须设置一点等待时间, 比如 time.sleep(2), 等待固定的 2 秒
# 下面是更智能的等待方案
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'article-container')))

# page_source 里面会包含 Ajax 请求到的数据
# 因为浏览器自动会帮助我们发送 Ajax 请求
text = driver.page_source

# 用 xpath 语法提取数据
element = etree.HTML(text)
article_element_list = element.xpath('//div[contains(@class, "article-container")]')
for article_element in article_element_list:

    title = article_element.xpath('./h5/a/text()')[0]
    url = article_element.xpath('./h5/a/@href')[0]
    desc = article_element.xpath('./p/text()')[0]

    print(title)
    print(url)
    print(desc)
    print('=' * 50)

# 关闭浏览器
driver.close()
"""
打印输出:
Python入门视频
https://study.163.com/course/introduction/1211262812.htm?share=2&shareId=480000002210461
如果只选一门编程语言来学习, 就学 Python 吧
==================================================
Python Pandas Excel 办公自动化
https://study.163.com/course/introduction/1209966922.htm?share=2&shareId=480000002210461
用python 的pandas 库进行数据分析, 来操作excel表格, 实现办公自动化。
==================================================
Python Web 接单实战
https://study.163.com/course/introduction/1211591811.htm?share=2&shareId=480000002210461
学习使用 flask 进行 python web 开发
==================================================
...
"""
