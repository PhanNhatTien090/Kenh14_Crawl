# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Kenh14Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    URL = scrapy.Field()
    Title = scrapy.Field()
    Consult = scrapy.Field()
    AuthorName = scrapy.Field()
    DateTime = scrapy.Field()
    
