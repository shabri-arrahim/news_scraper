import scrapy
import json
from scrapy.selector import Selector
from kompas.items import KompasItem


class Kompastrd(scrapy.Spider):
    name = "kompastrd"
    allowed_domains = ["kompas.com"]

    f = open('..\kompas\kompasindex.json', 'r')
    urls = json.load(f)

    start_urls = [url['link'] for url in urls][0:1000]

    def parse(self, response):

        item = KompasItem()
        item['content'] = " ".join(Selector(response).xpath('//div[@class="read__content"]//text()').getall()).strip()

        yield item
