# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class Hao6vSpider(scrapy.Spider):
    name = 'hao6v'
    allowed_domains = ['www.hao6v.com']
    start_urls = ['http://www.hao6v.com/']

    article_url = LinkExtractor(allow='http://www.hao6v.com/dy')
    print('article_urlarticle_url', article_url)
    rules = [
        Rule(article_url, callback='parseCategory', follow=True)
    ]



    def parse(self, response):
        print('首页', response.text)

    def parseCategory(self, response):
        print('内容在哪里', response.text)
