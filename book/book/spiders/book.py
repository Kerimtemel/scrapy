import scrapy

class BookSpider(scrapy.Spider):
    name = "book_child"
    file = open("child_book.txt", "w", encoding="utf-8")

    def start_requests(self):
        urls = ["https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=22"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(0, 15):
            book_name = response.css(".name.ellipsis a span::text")[i].extract()
            author = response.css(".author.compact.ellipsis a.alt::text")[i].extract()
            price = response.css("span.value::text")[i].extract()
            self.file.write("**{}**\nkitap ismi = {}\nyazar = {}\nfiyat = {}₺\n\n".format(i + 1, book_name, author, price))
