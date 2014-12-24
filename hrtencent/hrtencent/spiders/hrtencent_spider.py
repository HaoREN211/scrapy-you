__author__ = 'xiao'
import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from hrtencent.items import *
from hrtencent.log import *


class HrtencentSpider(CrawlSpider):
    name = "hrtencent"
    allowed_domains = ["tencent.com"]
    start_urls = [
        # "http://hr.tencent.com/position.php?start=%d" % d for d in range(0, 20, 10)
        "http://hr.tencent.com/position.php?start=0"
    ]
    rules = [
        Rule(sle(allow=("/position_detail.php\?id=\d*.*", )), follow=False, callback='parse_2'),
        # Rule(sle(allow=("/position.php\?&start=\d{,2}#a")), follow=True, callback='parse_1')
    ]
# li = site.css('.squareli li::text')

    def parse_2(self, response):
        items = []
        sel = Selector(response)
        site = sel.css('.tablelist')[0]
        item = PositionDetailItem()
        item['title'] = site.css('.h #sharetitle::text').extract()[0]
        item['location'] = site.css('.bottomline td::text').extract()[0]
        item['type'] = site.css('.bottomline td::text').extract()[1]
        item['people'] = site.css('.bottomline td::text').extract()[2]
        item['link'] = response.url
        li = site.css('.squareli li::text')
        item['duty'] = li.extract()[0]
        temp = []
        for i in range(1, len(li)):
            temp.append(li.extract()[i])
        item['skills'] = temp
        items.append(item)
        print repr(item).decode("unicode-escape") + '\n'
        self.parse_1(response)
        return items

    def parse_1(self, response):
        info('parsed '+str(response))

    # def _process_request(self, request):
    #     info('process ' + str(request))
    #     return request