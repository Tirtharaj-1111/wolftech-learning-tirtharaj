import scrapy
from ..items import FourscrapeItem


class ZclSpider(scrapy.Spider):
    name = 'zcl'
    allowed_domains = ['zsm-czest.logintrade.net']
    start_urls = ['https://zsm-czest.logintrade.net/rejestracja/ustawowe.html?page=1']

    def parse(self, response):
        items = FourscrapeItem()
        table = response.css("table.przetargi > tbody > tr")
        print('No. of rows in table:', len(table))
        for each_row in table:
            title = each_row.css("a::text").extract()
            entityIdAtSource = each_row.css(".przetarg_znak::text").extract()
            openDate = each_row.css(".data:nth-child(4)::text").extract()
            closeDate = each_row.css(".data:nth-child(5)::text").extract()
            items['title'] = title[0].strip()
            items['entityIdAtSource'] = entityIdAtSource[0].strip()
            items['openDate'] = openDate[0].strip()
            items['closeDate'] = closeDate[0].strip()
            yield items
        nxt_page = response.css("#content div.pagination > font > a:nth-child(5)::attr(href)").get()

        if nxt_page is not None:
            yield response.follow(nxt_page, callback=self.parse)
