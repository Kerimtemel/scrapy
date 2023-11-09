import scrapy
from datetime import datetime, timedelta

class weather(scrapy.Spider):
    name = "weather"
    start_urls = ["https://www.accuweather.com/tr/tr/aydin/317040/daily-weather-forecast/317040"]
    file = open("weather.txt", "w", encoding="utf-8")

    def parse(self, response):
        # Başlangıç tarihini belirle (6 Ekim 2023)
        start_date = datetime(2023, 10, 6)

        for i in range(0, 20):
            max_temp = response.css("span.high::text")[i].extract()
            min_temp = response.css("span.low::text")[i].extract()
            day = response.css("span.module-header.dow.date::text")[i].extract()

            # Tarih değerini formatla ve metin dosyasına yaz
            formatted_date = start_date.strftime("%d %B")
            self.file.write("{}  {}\tMaks :{}\tMin ={}\n".format(day,formatted_date, max_temp, min_temp))

            # Tarih değerini bir gün artır
            start_date += timedelta(days=1)
