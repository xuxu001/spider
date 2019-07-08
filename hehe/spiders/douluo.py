# -*- coding: utf-8 -*-
import scrapy
from hehe.items import HeheItem

class DouluoSpider(scrapy.Spider):
    name = 'douluo'
    allowed_domains = ['www.yuyouge.com']
    start_urls = ['https://www.yuyouge.com/book/980/']

    def parse(self, response):
        count_lsit = response.xpath("//*[@id='chapters-list']/li")
        # print(count_lsit)
        for cou in count_lsit:
            item={}
            item['name'] =cou.xpath(".//a/text()").extract_first()

            item['heh'] = cou.xpath(".//a/@href").extract()
            # print(item)
            item['heh'] =["https://www.yuyouge.com"+ i for i in item['heh']]
            # # yield item
            # print(item)
            for url in item['heh']:

                yield scrapy.Request(
                    url,
                    callback=self.parse1,
                    meta={"item":item}
                )

    def parse1(self,response):
        item = response.meta["item"]
        item['content'] =response.xpath("//*[@id='txtContent']/text()").extract_first()
        print(item)