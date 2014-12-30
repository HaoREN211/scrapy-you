# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    lagou_url = scrapy.Field()
    abbreviation = scrapy.Field()
    fullname = scrapy.Field()
    lagou_valid = scrapy.Field()
    brief = scrapy.Field()
    introduction = scrapy.Field()
    jobs_count = scrapy.Field()

    location = scrapy.Field()
    field = scrapy.Field()
    size = scrapy.Field()
    homepage = scrapy.Field()

    labels = scrapy.Field()


class JobItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    requirement = scrapy.Field()

