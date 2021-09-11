import requests
from lxml import etree


# 注意: 请由始至终都用 session 来发请求
session = requests.Session()

# 1. 因为后面需要用 post 请求, 先 get 请求"登录页"获取 csrftoken
# 如果没有开启 csrf 可以省略这一步
element = etree.HTML(session.get("https://anipython.com/accounts/login/").text)
csrftoken = element.xpath('//input[@name="csrfmiddlewaretoken"]/@value')[0]

# 2. 用 post 请求到"登录页"模拟登录一次
login_data = {
    "login": "test_user",
    "password": "tu123456789",
    "csrfmiddlewaretoken": csrftoken,
    "remember": 'on'
}
headers = {
    # 绝大多数的网站都需要提供 User-Agent
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    # 后端使用 django-allauth 要求提供 Referer
    "Referer": "https://anipython.com/accounts/login/",
}
res = session.post(url="https://anipython.com/accounts/login/", data=login_data, headers=headers)
assert res.status_code == 200, '登录请求错误'

# 3. 此时 session 已经保存了登录信息
# 可以直接使用 session 发 get 请求来获取"个人中心页"的内容
element = etree.HTML(session.get("https://anipython.com/user/profile/").text)
result = element.xpath('//h3//text()')
print(result)
# ['test_user', '\xa0的个人中心']
