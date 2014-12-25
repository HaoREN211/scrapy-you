# -*- coding: utf-8 -*-

# Scrapy settings for hrtencent project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'hrtencent'

SPIDER_MODULES = ['hrtencent.spiders']
NEWSPIDER_MODULE = 'hrtencent.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hrtencent (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'hrtencent.middleware.CustomHttpProxyMiddleware': 400,
    'hrtencent.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    # 'scrapy_mongodb.MongoDBPipeline': 300,
    'hrtencent.pipelines.JsonExportPipeline': 2,
}

LOG_FILE = 'hrtencent.log'
LOG_LEVEL = 'INFO'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB = "company"
MONGODB_COLLECTION = "tencent"
COOKIES_ENABLED = False