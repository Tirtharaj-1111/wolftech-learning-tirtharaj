import scrapy
from ..items import FivescrapeItem

# Method-1
# class AmzSpider(scrapy.Spider):
#     name = 'amz'
#     page_number = 2
#     allowed_domains = ['amazon.com']
#     start_urls = ['https://www.amazon.in/gp/bestsellers/books/ref=allbestsellers_Vsn/?ie=UTF8&pf_rd_p=5c5c3605-dbd4-4b97-8b60-d0401e2ffb1c&pf_rd_r=FJRVGS1R8BKHCGPCPDXF&pf_rd_s=books-subnav-flyout-content-1&pf_rd_t=SubnavFlyout&ref_=sn_gfs_co_books-best-sellers_AB_1']
#
#     def parse(self, response):
#         items = FivescrapeItem()
#
#         product_collection_selector = response.css("#gridItemRoot")
#
#         for each_product in product_collection_selector:
#             product_name = each_product.css(".a-link-normal span div::text").extract()
#             product_author = each_product.css(".a-size-small ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
#             product_price = each_product.css("._cDEzb_p13n-sc-price_3mJ9Z::text").extract()
#             product_imagelink = each_product.css(".p13n-product-image::attr(src)").extract()
#
#             items['product_name'] = product_name
#             items['product_author'] = product_author
#             items['product_price'] = product_price
#             items['product_imagelink'] = product_imagelink
#             yield items
#
#             next_page = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg=" +
#             str(AmzSpider.page_number)
#
#             if next_page is not None:
#                 yield response.follow(next_page, callback=self.parse)


# Method-2
class AmzSpider(scrapy.Spider):
    name = 'amz'
    allowed_domains = ['amazon.com']
    url = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_2?ie=UTF8&pg={}'

    def start_requests(self):
        for i in range(1, 3):
            yield scrapy.Request(self.url.format(i))

    def parse(self, response):
        items = FivescrapeItem()

        product_collection_selector = response.css("#gridItemRoot")

        for each_product in product_collection_selector:
            product_name = each_product.css(".a-link-normal span div::text").extract()
            product_author = each_product.css(".a-size-small ._cDEzb_p13n-sc-css-line-clamp-1_1Fn1y::text").extract()
            product_price = each_product.css("._cDEzb_p13n-sc-price_3mJ9Z::text").extract()
            product_imagelink = each_product.css(".p13n-product-image::attr(src)").extract()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_price'] = product_price
            items['product_imagelink'] = product_imagelink
            yield items
