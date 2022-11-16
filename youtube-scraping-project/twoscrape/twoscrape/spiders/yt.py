import scrapy
from ..items import TwoScrapeItem


class YtSpider(scrapy.Spider):
    name = 'yt'
    allowed_domains = ['www.youtube.com']
    start_urls = ['https://www.youtube.com/']

    def parse(self, response):
        all_cards = response.css("div.style-scope.yt-horizontal-list-renderer > ytd-grid-video-renderer")
        items = TwoScrapeItem()
        for yc in all_cards:
            title = yc.css("a.yt-simple-endpoint.style-scope.ytd-grid-video-renderer::text").extract()
            channel = yc.css(".yt-formatted-string::text").extract()
            views = yc.css("#metadata-line > span:nth-child(1)::text").extract()
            posted = yc.css("#metadata-line > span:nth-child(2)::text").extract()
            items['title'] = title
            items['channel'] = channel
            items['views'] = views
            items['posted'] = posted
            yield items

