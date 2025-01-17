import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.amazon.ca"]
    start_urls = ["https://www.amazon.ca/Best-Sellers-generic/zgbs/?ref_=nav_cs_bestsellers"]

    def parse(self, response):
        #crawl các link category trong trang best seller
        category = response.css('div._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz a::attr(href)').getall()
        subcategory = response.css('div._p13n-zg-nav-tree-all_style_zg-browse-group__88fbz a::attr(href)').getall()
        product_link = response.css('div.p13n-sc-uncoverable-faceout > a::attr(href)').getall()

        
        title = response.css('span.a-size-large::text').get().strip()
        price = response.css('span.a-offscreen::text').get()
        review = response.css('#acrCustomerReviewText::text').get()
        brand = response.xpath("//td[span[text()='Brand']]/following-sibling::td/span/text()").get()
        stars = response.css('span.a-icon-alt::text').get()
        comments= response.css('a.a-link-normal._Y3Itc_aspect-link_TtdmS._Y3Itc_aspect-link-symbol_23T9N::text').getall()
        productCategory = response.css('a.nav-b span.nav-a-content::text').get().strip()

        pass
