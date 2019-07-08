# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        for i in range(10):
            item={}
            item['comm_from']="itcase"
            logger.warning(item)
            yield item
