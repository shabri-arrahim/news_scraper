import scrapy
import json
from scrapy.selector import Selector
from kompas.items import KompasItem


class Kompastrd(scrapy.Spider):
    name = "kompastrd"
    allowed_domains = ["kompas.com"]

    # f = open('..\kompas\kompasindex.json', 'r')
    # urls = json.load(f)

    start_urls = None #[url['link'] for url in urls]

    def parse(self, response):

        # article = Selector(response).xpath('//div[@class="contentArticle box-shadow-new"]')

        item = KompasItem()
        item['content'] = Selector(response).xpath('//div[@class="read__content"]//text()').getall()

        yield item
