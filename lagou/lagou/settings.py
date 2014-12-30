# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagou (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
    'lagou.middleware.CustomHttpProxyMiddleware': 400,
    'lagou.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    # 'scrapy_mongodb.MongoDBPipeline': 300,
    'lagou.pipelines.JsonExportPipeline': 2,
}

LOG_FILE = 'lagou.log'
LOG_LEVEL = 'INFO'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB = "company"
MONGODB_COLLECTION = "lagou"
MONGODB_COLLECTION2 = "lagou_job"
COOKIES_ENABLED = False