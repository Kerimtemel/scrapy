import scrapy

class magazin(scrapy.Spider):
    name = "magazin"
    file = open("magazin.txt","w",encoding="utf-8")
    start_urls = ["https://www.haberler.com/magazin/"]

    def parse(self,response):
        for j in range(0,20):
            magazin =  magazin = response.css("p.hbBoxText::text")[j].extract()
            self.file.write("{} = {}\n".format(j+1,magazin))





class ekonomi(scrapy.Spider):
    name = "ekonomi"
    file = open("ekonomi.txt"",w",encoding="utf-8")
    start_urls = ["https://www.haberler.com/ekonomi/"]

    def parse(self,response):
        for i in range(0, 20):
            ekonomi = response.css("p.hbBoxText::text")[i].extract()
            self.file.write("{} = {}\n".format(i + 1, ekonomi))


class sondakika(scrapy.Spider):
    name = "sondakika"
    file = open("son_dakika.txt","w", encoding="utf-8")
    start_urls = ["https://www.haberler.com"]

    def parse(self, response):
        for k in range(0,20):
            sondakika = response.css("p.hbBoxText::text")[k].extract()
            self.file.write("{} = {}\n".format(k + 1, sondakika))


