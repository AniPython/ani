from selenium import webdriver

# 1. webdriver 的一些设置
profile = webdriver.FirefoxProfile()
# 2表示自定义文件夹 0表示保存到桌面
profile.set_preference('browser.download.folderList', 2)
# 设置默认的保存文件夹
profile.set_preference('browser.download.dir', "/Users/yi/Downloads")
# 不要过问, 直接下载保存到本地
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'application/zip,text/plain,application/vnd.ms-excel,text/csv,text/comma-separated-values,application/octet-stream,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document')

# 如果 geckodriver 没有放到 python 的环境变量中, 会出现以下的异常信息
# Message: 'geckodriver' executable needs to be in PATH.
driver = webdriver.Firefox(firefox_profile=profile)

# 2. 打开下载按钮所在的页面
host = 'http://127.0.0.1:8000'
driver.get(f"{host}/crawler/6/")

# 3. 用 xpath 语法找到下载按钮并点击
driver.find_element_by_xpath('//div[@class="card-body"]/a[@class="btn btn-primary"]').click()

# 4. 下载完成后自动关闭 driver
driver.close()
