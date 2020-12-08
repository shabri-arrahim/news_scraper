import scrapy
from scrapy.selector import Selector
from kompas.items import KompasItem


class KompasSpider(scrapy.Spider):
    name = "kompas"
    allowed_domains = ["kompas.com"]
    # Kategori index berita yang tersedia
    """'news','tren','health','food''edukasi',
        'inspirasli','money','tekno','lifestyle',
        'homey','property','bola','travel','otomotif',
        'sains','hype','vik','kolom','jeo'"""
    # Sesuaikan jumlah page index berdasarkan kategori              
    page = range(1, 229)
    # Ganti nama kategoti berdasarkan index list kategori diatas
    # http://indeks.kompas.com/?site=[sisipkan kategori diposisi ini]&page=
    urls = ["http://indeks.kompas.com/?site=health&page="+str(i) for i in page]
    start_urls = urls
            
    def parse(self, response):

        indeks = Selector(response).xpath('//div[@class="article__list clearfix"]')

        for indek in indeks:
            item = KompasItem()
            item['title'] = indek.xpath('div[@class="article__list__title"]/h3/a/text()').extract_first()
            item['link'] = indek.xpath('div[@class="article__list__title"]/h3/a/@href').extract_first()+"?page=all#page2"
            item['images'] = indek.xpath('div[@class="article__list__asset clearfix"]/div/img/@src').extract_first()
            item['category'] = indek.xpath('div[@class="article__list__info"]/div[@class="article__subtitle article__subtitle--inline"]/text()').extract_first()
            item['date'] = indek.xpath('div[@class="article__list__info"]/div[@class="article__date"]/text()').extract_first()
            item['desc'] = ""

            yield item
