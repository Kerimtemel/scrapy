import scrapy
class movie(scrapy.Spider):
    name = "movie"

    file = open("movie.txt" ,"w" ,encoding = "utf-8")
    start_urls = ["https://boxofficeturkiye.com/tum-zamanlar/seyirci-rekorlari/yabanci-filmler"]


    def parse(self, response):
        for j in range(1, 41, 2):
            movie_views = response.css("td.column--numeric::text")[j].extract()


        for i in range(0,20):
            movie_name = response.css("a.movie-link::text")[i].extract()
            movie_release_date = response.css("span.release-date::text")[i].extract()
            self.file.write("{} = {}\nrelease date={}\nviews = {}\n\n".format(i + 1, movie_name,movie_release_date,movie_views))

