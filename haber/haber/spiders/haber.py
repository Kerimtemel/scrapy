import sys
import scrapy
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser

class HaberSpider(scrapy.Spider):
    name = "haber"
    start_urls = ["https://www.haberler.com"]

    def parse(self, response):
        haberler = []
        for i in range(0, 20):
            headline = response.css("p.hbBoxText::text")[i].extract()
            haberler.append(f"{i + 1} = {headline}")

        with open("haber.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(haberler))

class HaberApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Haberler Uygulaması")
        self.setGeometry(100, 100, 800, 600)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(10, 10, 780, 580)

        self.showHaberler()

    def showHaberler(self):
        try:
            with open("haber.txt", "r", encoding="utf-8") as file:
                haberler = file.readlines()
                for haber in haberler:
                    self.text_browser.append(haber.strip())
        except Exception as e:
            self.text_browser.append("Haberler yüklenirken bir hata oluştu: " + str(e))

def main():
    # Scrapy Spider'ı başlatmak için
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(HaberSpider)
    process.start()

    # PyQt5 uygulamasını başlatmak için
    app = QApplication(sys.argv)
    haber_app = HaberApp()
    haber_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
# ekonomi = response.css("p.hbBoxText::text").extract()
#https://www.haberler.com/ekonomi/
#  magazin = response.css("p.hbBoxText::text").extract()
#https://www.haberler.com/magazin/