import scrapy 
from Kenh14.items import Kenh14Item


class Kenh14DataSpider(scrapy.Spider):
    name = "Kenh14Data"
    allowed_domains = ["kenh14.vn"]
    
    
    def start_requests(self):
        yield scrapy.Request(url='https://kenh14.vn/', callback=self.parse)

    def parse(self, response):
        ArticleLists = response.xpath('.//h3/a/@href').getall()
        for ArticleK14Items in ArticleLists:
            k14item = Kenh14Item()
            k14item['URL'] = response.urljoin(ArticleK14Items)
            request = scrapy.Request(url = response.urljoin(ArticleK14Items), callback=self.parsearticlepage)
            request.meta['articledata'] = k14item
            yield request
    
    def parsearticlepage(self, response):
        k14item = response.meta['articledata']
        k14item['Title'] = response.xpath('normalize-space(string(.//div[2]/div/div[1]/div[1]/div[1]/h1))').get()
        k14item['Consult'] = response.xpath('normalize-space(string(.//div[2]/div[3]/div[1]/div[3]/div[1]/div/ul/li[1]/a/@title))').get()
        k14item['AuthorName'] = response.xpath('normalize-space(string(.//div[2]/div/div[1]/div[1]/div[1]/div[2]/span[1]))').get()
        k14item['DateTime'] = response.xpath('normalize-space(string(.//div[2]/div/div[1]/div[1]/div[1]/div[2]/span[3]))').get()
        yield k14item    