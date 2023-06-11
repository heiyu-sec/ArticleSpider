import scrapy


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]

    def parse(self, response):
       #url =  response.xpath('//*[@id="entry_743643"]/div[2]/h2/a/@href').extract_first("")
       url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract()
       pass
