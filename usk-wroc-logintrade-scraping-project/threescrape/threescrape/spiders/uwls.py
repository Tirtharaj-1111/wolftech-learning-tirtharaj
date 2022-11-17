import scrapy
from ..items import ThreescrapeItem


class UwlsSpider(scrapy.Spider):
    name = 'uwls'
    allowed_domains = ['usk-wroc.logintrade.net']
    start_urls = ['https://usk-wroc.logintrade.net/rejestracja/przetargi.html']

    def parse(self, response):
        # title = response.css("a::text").extract()
        items = ThreescrapeItem()
        k = response.css("table.przetargi > tbody > tr")
        # print('abc', len(k))
        for row in k:
            title = row.css("a::text").extract()
            openDate = row.css(".data:nth-child(4)::text").extract()
            closeDate = row.css(".data:nth-child(5)::text").extract()
            items['title'] = title[0].strip()
            items['openDate'] = openDate[0].strip()
            items['closeDate'] = closeDate[0].strip()
            yield items


