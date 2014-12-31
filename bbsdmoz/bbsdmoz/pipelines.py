# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo
from scrapy import signals
from bbsdmoz.items import BbsItem
from scrapy.contrib.exporter import XmlItemExporter
from scrapy.conf import settings


class XmlWritePipeline(object):
    # def __init__(self):
    #     pass
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     pipeline = cls()
    #     crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    #     crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    #     return pipeline
    #
    # def spider_opened(self, spider):
    #     self.file = open('bbsData.xml', 'wb')
    #     self.expoter = XmlItemExporter(self.file)
    #     self.expoter.start_exporting()
    #
    # def spider_closed(self, spider):
    #     self.expoter.finish_exporting()
    #     self.file.close()
    #
    # def process_item(self, item, spider):
    #     self.expoter.export_item(item)
    #     return item
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # self.exporter.export_item(item)
        valid = True
        for data in item:
            # here we only check if the data is not null
            # but we could do any crazy validation we want
            if not data:
                valid = False
                raise DropItem("Missing %s of blogpost from %s" % (data, item['url']))
        if valid:
            if len(item) > 2:
                if isinstance(item, BbsItem):
                    self.collection.insert(dict(item))
        return item