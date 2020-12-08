import scrapy
import json
from scrapy.selector import Selector
from kompas.items import KompasItem


class Kompastrd(scrapy.Spider):
    name = "kompastrd"
    allowed_domains = ["kompas.com"]

    f = open('..\kompas\kompasindex_tekno.json', 'r')
    urls = json.load(f)

    start_urls = [url['link'] for url in urls][0:1000]

    def parse(self, response):

        item = KompasItem()
        arr_text = Selector(response).xpath('//div[@class="read__content"]//text()').getall()
        for i, cnt in enumerate(arr_text):
            if cnt.strip().lower() == 'baca juga:':
                arr_text.pop(i)
                arr_text.pop(i)
            elif(cnt.strip().lower().find('baca juga:') != -1):
                arr_text.pop(i)

        clean_text = " ".join(arr_text).strip()
        item['content'] = clean_text

        yield item
