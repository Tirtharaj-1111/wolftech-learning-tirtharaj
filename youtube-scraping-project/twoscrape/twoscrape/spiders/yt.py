import scrapy
from ..items import TwoScrapeItem


class YtSpider(scrapy.Spider):
    name = 'yt'
    allowed_domains = ['www.youtube.com']
    start_urls = ['https://www.youtube.com/channel/UCtFRv9O2AHqOZjjynzrv-xg']

    def parse(self, response):
        # all_cards = response.css("div.style-scope.yt-horizontal-list-renderer > ytd-grid-video-renderer")
        items = TwoScrapeItem()
        # for yc in all_cards:

        title = response.css("h3 a::text").extract()
        channel = response.css(".yt-formatted-string::text").extract()
        views = response.css("#metadata-line .ytd-grid-video-renderer:nth-child(1)::text").extract()
        posted = response.css("#metadata-line .ytd-grid-video-renderer+ .ytd-grid-video-renderer::text").extract()
        items['title'] = title
        items['channel'] = channel
        items['views'] = views
        items['posted'] = posted
        yield items

