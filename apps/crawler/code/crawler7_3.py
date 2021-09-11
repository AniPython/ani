import time

from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

host = 'http://anipython.com'

login_url = f"{host}/user/login/"  # 用于登录
profile_url = f"{host}/user/profile/"  # 获取内容

# 打开 Chrome 浏览器
driver = webdriver.Chrome()

# 访问登录页
driver.get("https://anipython.com/accounts/login/")

# 输入用户名
username_input = driver.find_element_by_name('login')
username_input.clear()
username_input.send_keys('test_user')

# 输入密码
username_input = driver.find_element_by_name('password')
username_input.clear()
username_input.send_keys('tu123456789')

# 点击登陆
login_btn = driver.find_element_by_xpath('//button[@type="submit"]')
login_btn.click()

# 等待, 最多等待60秒, 如果有更复杂的登录操作(图形验证码, 扫码登陆等), 可以在这60秒内手动操作
wait = WebDriverWait(driver, 60)

# 等待直到出现"退出"按钮(出现"退出"的按钮表示登录成功)
# 如果60秒都等不到, 程序会抛异常
wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, '退出')))

# 访问个人中心
driver.get("https://anipython.com/user/profile/")

# driver.page_source 是当前页面 text 内容
element = etree.HTML(driver.page_source)

# 也可以配合使用 xpath 语法进行解析
result = element.xpath('//h3//text()')
print(result)
# 输出: ['test_user', '\xa0的个人中心']
time.sleep(1)
# 最后退出浏览器
driver.close()
