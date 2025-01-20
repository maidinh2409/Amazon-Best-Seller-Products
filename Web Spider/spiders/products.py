import scrapy
from ..items import ProductItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.amazon.ca"]
    start_urls = ["https://www.amazon.ca/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers"]

    def parse(self, response):
        category = response.css('div._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz a::attr(href)').getall()
        for category_link in category:
            yield response.follow(category_link, callback = self.parse_category)
        
    def parse_category(self, response):
        subcategory = response.css('div._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz a::attr(href)').getall()
        for subcategory_link in subcategory:
            yield response.follow(subcategory_link, callback = self.parse_subcategory)

    def parse_subcategory(self, response):
        product_link = response.css('div.p13n-sc-uncoverable-faceout > a::attr(href)').getall()
        for product_links in product_link:
            yield response.follow(product_links, callback = self.parse_products)

    def parse_products(self, response):
        product = ProductItem()

        product['productName'] = response.css('span.a-size-large::text').get(default='').strip()
        product['productPrice'] = response.css('span.a-offscreen::text').get()
        product['numberReviews'] = response.css('#acrCustomerReviewText::text').get()
        product['productBrand'] = response.xpath("//td[span[text()='Brand']]/following-sibling::td/span/text()").get()
        product['numberStars'] = response.css('span.a-icon-alt::text').get()
        product['highlightedFeatures'] = response.css('a.a-link-normal._Y3Itc_aspect-link_TtdmS._Y3Itc_aspect-link-symbol_23T9N::text').getall()
        product['productCategory'] = response.css('a.nav-b span.nav-a-content::text').get(default='').strip()

        yield product
        
