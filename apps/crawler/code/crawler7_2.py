import requests
from lxml import etree

host = 'http://anipython.com'

login_url = f"{host}/user/login/"  # 用于登录
profile_url = f"{host}/user/profile/"  # 获取内容

# 注意: 请由始至终都用 session 来发请求
session = requests.Session()

# 1. 因为后面需要用 post 请求, 先 get 请求"登录页"获取 csrftoken
# 如果没有开启 csrf 可以省略这一步
element = etree.HTML(session.get(login_url).text)
csrftoken = element.xpath('//input[@name="csrfmiddlewaretoken"]/@value')[0]

# 2. 用 post 请求到"登录页"模拟登录一次
login_data = {
    "username": "test_user",
    "password": "tu123456789",
    "csrfmiddlewaretoken": csrftoken
}
session.post(url=login_url, data=login_data)

# 3. 此时 session 已经保存了登录信息
# 可以直接使用 session 发 get 请求来获取"个人中心页"的内容
element = etree.HTML(session.get(profile_url).text)
result = element.xpath('//div[@class="container"]//text()')
print(result)
# 输出: ['\n    ', '个人中心', '\n    ', '你的用户名是:&nbsp', 'test_user', '\n']
