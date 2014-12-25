__author__ = 'xiao'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from moko.items import MokoItem, DmozItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class MokoSpider(CrawlSpider):
    name = "moko"
    allowed_domains = ['moko.cc']
    start_urls = ["http://www.moko.cc/post/aaronsky/list.html"]
    # start_urls = ["http://www.moko.cc/post/1057921.html"]
    rules = [Rule(SgmlLinkExtractor(allow=('/post/\d*\.html',)), callback='parse_img', follow=False),
    ]
    #

    def parse(self, response):
        item = MokoItem()
        sel = Selector(response)
        image_urls = sel.xpath('//img/@src2').extract()
        item['image_urls'] = [x for x in image_urls]
        return item
        # for divs in sel.xpath('//div[@class="pic dBd"]'):
        # img_url = divs.xpath('.//img/@src2').extract()[0]
        #     urlItem['image_urls'].append(img_url)
        # print urlItem['image_urls']
        # return urlItem

        #维基百科
        # allowed_domains = ["wikipedia.org"]
        # start_urls = [
        #     "http://en.wikipedia.org/wiki/Pune"
        # ]
        #
        # def parse(self, response):
        #     hxs = HtmlXPathSelector(response)
        #     item = DmozItem()
        #     image_urls = hxs.select('//img/@src').extract()
        #     item['image_urls'] = ["http:" + x for x in image_urls]
        #     return item