import scrapy
class QuotesSpider(scrapy.Spider):
    name = "books"
    quote_count = 1
    file = open("books.txt" ,"a" ,encoding = "utf-8")
    start_urls = [
        'https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=16',
    ]

    def parse(self, response):


        for i in range(0,20):
            book_name = response.css("div.name.ellipsis a span::text")[i].extract()
            book_author =response.css("div.author span a span::text")[i].extract()
            book_price = response.css("div.price-new span.value::text")[i].extract()
            self.file.write("\t\t\t\t\t***{}kitap****\nİSİM:{}\tYAZAR:{}\tÜCRET:{}₺\n".format(i+1,book_name,book_author,book_price))






































