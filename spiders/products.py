import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.amazon.ca"]
    start_urls = ["https://www.amazon.ca/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers"]

    def parse(self, response):
        category = response.css('div._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz a::attr(href)').getall()
        product_link = response.css('div.p13n-sc-uncoverable-faceout > a::attr(href)').getall()

        pass
