# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings
from lagou.items import LagouItem, JobItem


class JsonExportPipeline(object):

    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.collection2 = db[settings['MONGODB_COLLECTION2']]

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
                if isinstance(item, LagouItem):
                    self.collection.insert(dict(item))
                    log.msg("Item wrote to MongoDB database %s/%s" %
                            (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                            level=log.DEBUG, spider=spider)
                if isinstance(item, JobItem):
                    self.collection2.insert(dict(item))
                    log.msg("Item wrote to MongoDB database %s/%s" %
                            (settings['MONGODB_DB'], settings['MONGODB_COLLECTION2']),
                            level=log.DEBUG, spider=spider)
        return item
