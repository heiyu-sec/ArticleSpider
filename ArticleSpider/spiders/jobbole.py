import scrapy


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    def parse(self, response):
        response.xpath("/html/body/div[2]/div[2]/div[4]/div[1]/div[2]/h2/a")
        pass
