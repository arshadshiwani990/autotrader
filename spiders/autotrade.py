import scrapy


class AutotradeSpider(scrapy.Spider):
    name = 'autotrade'
    allowed_domains = ['classics.autotrader.com']
    start_urls = ['http://classics.autotrader.com/']

    def parse(self, response):
        pass
