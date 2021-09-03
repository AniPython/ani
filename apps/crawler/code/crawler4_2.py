# Ani.ani.spiders.crawler4.py
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Crawler4Spider(CrawlSpider):
    # 爬虫的名字, 爬虫可以有多个, 用于指定运行的是哪一个
    name = 'crawler4'
    # 允许进行爬取的域名, 比如 allowed_domains=['qq.com'], 就不会爬到 baidu.com
    allowed_domains = ['anipython.com']
    # 第一次请求的地址, 此请求默认自动发送
    start_urls = ['http://anipython.com/crawler/4/?page=1']

    rules = (
        # r'/crawler/4/\?page' 是正则匹配外层的 url, 每个请求到的页面都会自动提取
        # callback 一般是用于写提取数据的逻辑
        # follow=True 表示匹配到新的页面, 继续向这个页面发送请求, 因为有"下一页"的按钮中的url
        # follow=True 就可能获取到全部的外层页面
        Rule(LinkExtractor(allow=r'/crawler/4/\?page'), callback=None, follow=True),

        # r'/crawler/4/\d+' 是正则匹配里层详情的 url
        # 详情页需要提取数据, 所以指定 callback
        Rule(LinkExtractor(allow=r'/crawler/4/\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//div[@class="card-body"]//h4[@class="title"]/a/text()').get()
        item['url'] = response.xpath('//div[@class="card-body"]//h4[@class="title"]/a/@href').get()
        item['desc'] = response.xpath('//div[@class="card-body"]//p/text()').get()
        print("*****")
        print(item)
        return item