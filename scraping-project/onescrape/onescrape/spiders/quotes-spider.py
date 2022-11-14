import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'qts'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        all_div_cards = response.css('div.quote')

        # title = response.css('title::text').extract()
        for q in all_div_cards:
            quote = q.css('span.text::text').extract()
            author = q.css('span.author::text').extract()
            tags = q.css('.tag::text').extract()
            yield {'quote': quote,
                   'author': author,
                   'tags': tags}


