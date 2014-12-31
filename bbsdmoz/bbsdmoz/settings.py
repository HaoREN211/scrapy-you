# -*- coding: utf-8 -*-

# Scrapy settings for bbsdmoz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsdmoz'
CONCURRENT_REQUESTS = 200
LOG_LEVEL = 'INFO'
SPIDER_MODULES = ['bbsdmoz.spiders']
NEWSPIDER_MODULE = 'bbsdmoz.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsdmoz (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'bbsdmoz.pipelines.XmlWritePipeline': 1000,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DB = "company"
MONGODB_COLLECTION = "bbs"
COOKIES_ENABLED = False