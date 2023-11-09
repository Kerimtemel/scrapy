import scrapy

class magazin(scrapy.Spider):
    name = "magazin"
    file = open("magazin.txt","w",encoding="utf-8")
    start_urls = ["https://www.haberler.com/magazin/"]
    def parse(self,response):
        for i in range(0,20):
            magazin = response.css("p.hbBoxText::text")[i].extract()
            self.file.write("{} = {}\n".format(i+1,magazin))
