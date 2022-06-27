# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeautyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image = scrapy.Field()
    dirname = scrapy.Field()
