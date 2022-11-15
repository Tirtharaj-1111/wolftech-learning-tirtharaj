import scrapy
from ..items import OnescrapeItem

class QuoteSpider(scrapy.Spider):
    name = 'qts'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # all_div_cards = response.css('div.quote')
        # title = response.css('title::text').extract()
        # for q in all_div_cards:
        #     quote = q.css('span.text::text').extract()
        #     author = q.css('.author::text').extract()
        #     tags = q.css('.tag::text').extract()
        #     yield {'quote': quote,
        #            'author': author,
        #            'tags': tags}

        # Method -2
        # all_div_cards = response.css('div.quote')
        # for q in all_div_cards:
        #     quote = q.css('span.text::text').extract()
        #     author = q.css('.author::text').extract()
        #     tags = q.css('.tag::text').extract()
        #
        #     x = {'quote': quote,
        #          'author': author,
        #          'tags': tags}
        #     print(x)

        #  Method -3
        all_div_cards = response.css('div.quote')
        items = OnescrapeItem()
        for q in all_div_cards:
            quote = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tags = q.css('.tag::text').extract()
            #  items container will contain scraped data and in every iteration,
            #  it will return items container filled with scraped data
            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags
            yield items
        print(type(items))