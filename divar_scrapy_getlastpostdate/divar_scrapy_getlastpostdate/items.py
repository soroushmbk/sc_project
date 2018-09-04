# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DivarScrapyGetlastpostdateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LastPostDateItem(scrapy.Item):
    lastpostdate = scrapy.Field()
    category = scrapy.Field()
    originsite = scrapy.Field()
    updatetime = scrapy.Field()
