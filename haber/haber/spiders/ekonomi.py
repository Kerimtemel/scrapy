import scrapy

class ekonomi(scrapy.Spider):
    name = "ekonomi"
    start_urls = ["https://www.haberler.com/ekonomi/"]
    file = open("ekomomi.txt","w",encoding="utf-8")


    def parse(self,response):
        for i in range(0,20):
            ekonomi = response.css("p.hbBoxText::text")[i].extract()
            self.file.write("{} = {}\n".format(i+1,ekonomi))
