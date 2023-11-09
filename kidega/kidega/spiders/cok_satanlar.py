import scrapy


class CokSatanlarSpider(scrapy.Spider):
    name = "cok_satanlar"
    allowed_domains = ["www.kidega.com"]
    start_urls = ["https://kidega.com/anasayfa-cok-satanlar-listesi/"]

    def parse(self, response):
        pass
