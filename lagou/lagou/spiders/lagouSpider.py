# -*- coding:utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from lagou.items import LagouItem, JobItem
from scrapy.http import Request


class lagouSpider(CrawlSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        'http://www.lagou.com/sitemap/'
    ]
    rules = [
        Rule(SgmlLinkExtractor(
            allow=(r"http://(.*)/\d+\.html",)),
            callback='parse_page',
            follow=False),
    ]

    def parse_page(self, response):

        sel = Selector(response)
        lagou = LagouItem()
        if sel.xpath("//input[@type='hidden']//@value").extract():
            lagou['lagou_url'] = sel.xpath("//input[@type='hidden']//@value").extract()[0]
        field = {}
        field.setdefault('abbreviation', "h2") #sel.css("h2::text").extract()[0]
        field.setdefault('fullname', ".fullname") #sel.css(".fullname::text").extract()[0]
        field.setdefault('lagou_valid', ".va") #sel.css(".va::text").extract()[0]
        field.setdefault('brief', ".oneword") #sel.css(".oneword::text").extract()[0]
        field.setdefault('introduction', ".c_intro") #sel.css(".oneword::text").extract()[0]
        field.setdefault('jobs_count', ".jobsTotal i") #sel.css(".jobsTotal i::text").extract()[0]

        for key, value in field.iteritems():
            s = sel.css("%s::text" % value)
            if s:
                lagou['%s' % key] = s[0].extract()
        if len(sel.css('.c_tags td::text')) > 6:
            lagou['location'] = sel.css('.c_tags td::text').extract()[1]
            lagou['field'] = sel.css('.c_tags td::text').extract()[3]
            lagou['size'] = sel.css('.c_tags td::text').extract()[5]
        if sel.xpath("//div[@class='c_tags']/table/tr/td/a/@href"):
            lagou['homepage'] = sel.xpath("//div[@class='c_tags']/table/tr/td/a/@href").extract()[0]
        temp = []

        labels = sel.css("#hasLabels li span")
        for i in range(0, len(labels)):
            temp.append(labels[i].css('span::text').extract()[0])
        lagou['labels'] = temp

        if sel.css(".jobsTotal i::text"):
            number = int(sel.css(".jobsTotal i::text").extract()[0])
            for i in range(number/10+1):
                url = "http://www.lagou.com/jobs/pl_%s.html?pageNo=%d" % (lagou['lagou_url'], i+1)
                yield Request(url,
                              meta={
                                  'company': lagou['abbreviation'],
                                  },
                              callback=self.parse_job)
        yield lagou

    def parse_job(self, response):

        sel = Selector(response)
        jobs = sel.css(".c_jobs li")
        for i in range(len(jobs)):
            items = JobItem()
            items['company'] = response.meta['company']
            items['title'] = jobs[i].css("span::text").extract()[0]
            items['location'] = jobs[i].css("span::text").extract()[1]
            items['date'] = jobs[i].css("span::text").extract()[2]
            items['requirement'] = jobs[i].css("div::text").extract()[0]
            yield items

#labels  spans[0].xpath("./text()").extract()[0]  spans = sel.css("#hasLabels li span")
#spans[0].css('span::text').extract()[0]  spans = sel.css("#hasLabels li span")
#location sel.css('.c_tags td::text').extract()[1]
#field sel.css('.c_tags td::text').extract()[3]
#size sel.css('.c_tags td::text').extract()[5]
#homepage sel.xpath("//div[@class='c_tags']/table/tr/td/a/@href").extract()[0]


