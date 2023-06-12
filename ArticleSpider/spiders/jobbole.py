import scrapy
import undetected_chromedriver

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["news.cnblogs.com"]
    start_urls = ["https://news.cnblogs.com"]
    custom_settings = {
        "COOKIES_ENABLED":True
    }

    def start_requests(self):
        #入口模拟登录拿到cookie，selenium控制浏览器会被一些网站识别出来
        import undetected_chromedriver.v2 as uc 
        browser = uc.Chrome()
        browser.get("https://account.cnblogs.com/signin")
        #自动化输入，自动化识别华东验证码
        input("回车继续：")
        cookies = browser.get_cookids()
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']

        for url in self.start_urls:
            #将cookie交给scrapy
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
            }
            yield scrapy.Request(url,cookies=cookie_dict,headers=headers,dont_filter=True)

    def parse(self, response):
       #url =  response.xpath('//*[@id="entry_743643"]/div[2]/h2/a/@href').extract_first("")
       url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract()
       pass
