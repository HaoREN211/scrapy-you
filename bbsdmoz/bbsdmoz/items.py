# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbsItem(scrapy.Item):
    url = scrapy.Field()
    forum = scrapy.Field()
    poster = scrapy.Field()
    content = scrapy.Field()
