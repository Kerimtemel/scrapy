import scrapy

class QuotesSpider(scrapy.Spider):
    name = "amazon"
    file = open("phone.txt", "a", encoding="utf-8")

    def start_requests(self):
        allowed_domains = ["amazon.com"]
        start_urls = [
            'https://www.amazon.com/s?k=smartphone&i=mobile&rh=n%3A7072561011%2Cp_n_feature_thirty-nine_browse-bin%3A113334728011%7C113334730011&dc&crid=NXPGGBNROYTB&qid=1696356851&rnid=113334702011&sprefix=smart+phon%2Caps%2C314&ref=sr_pg_1',
        ]


    def parse(self, response):
        for i in range(0, 20):
            model = response.css("span.a-size-medium.a-color-base.a-text-normal::text")[i].extract()

            self.file.write("**1**\nMODEL = {}\n".format(model))



