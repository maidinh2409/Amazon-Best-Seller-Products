import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.amazon.ca"]
    start_urls = ["https://www.amazon.ca/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers"]

    def parse(self, response):
        pass
