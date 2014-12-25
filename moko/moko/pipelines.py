# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from moko.items import MokoItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


# class MokoPipeline(object):
#     def __init__(self):
#         self.mfile = open('test.html', 'w')
#
#     def process_item(self, item, spider):
#         text = '<img src="' + item['url'] + '" alt = "" />'
#         self.mfile.writelines(text)
#
#     def close_spider(self, spider):
#         self.mfile.close()


# class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item