# -*- coding: utf-8 -*-

# Scrapy settings for moko project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'moko'

SPIDER_MODULES = ['moko.spiders']
NEWSPIDER_MODULE = 'moko.spiders'


DOWNLOADER_MIDDLEWARES = {
    'moko.middleware.CustomHttpProxyMiddleware': 400,
    'moko.middleware.CustomUserAgentMiddleware': 401,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'moko (+http://www.yourdomain.com)'
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1,
}
IMAGES_STORE = '/home/xiao/photo/moko'
LOG_FILE = 'moko.log'
LOG_LEVEL = 'INFO'
COOKIES_ENABLED = False
IMAGES_EXPIRES = 1   #1天内抓取的都不会被重抓
# IMAGES_THUMBS = {
# 'small': (50, 50),
# 'big': (270, 270),
# }
#压缩后存放在：<IMAGES_STORE>/thumbs/<size_name>/<image_id>.jpg
# 可以设置过滤下图片，设置方法如下：

# IMAGES_MIN_HEIGHT = 110
#
# IMAGES_MIN_WIDTH = 110