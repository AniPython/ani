"""
使用 requests 和 xpath
$ pip install requests
$ pip install lxml
如果安装出错可以尝试更换国内源
$ pip install -i https://pypi.doubanio.com/simple lxml
"""
import requests
from lxml import etree

# 1. 设置headers中的User-Agent, 发送请求, 获取响应
host = 'http://127.0.0.1:8000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
response = requests.get(f"{host}/crawler/2/", headers=headers)

# 2. 读取响应内容并解码成String
html_text = response.text

# 3. 把 String 字符串转成 Element 对象
html_element = etree.HTML(html_text)

# 4. 用 Element 对象的 xpath 方法提取想要的数据
result_list = html_element.xpath('//div[contains(@class,"card-body")][1]//text()')
result_list = [x.strip() for x in result_list if x.strip()]
print(result_list)
# 输出: ['静夜思', '李白', '床前明月光，', '疑是地上霜。', '举头望明月，', '低头思故乡。']
