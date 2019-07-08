# -*- coding: utf-8 -*-
import scrapy
from hehe.items import HeheItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/']

    def parse(self, response):
        list = response.xpath("//div[@id='content-left']/div")
        # print(list)
        for ls in list:
            item={}
            item['text']=ls.xpath(".//a/div/span/text()").extract_first()
            item['image']=ls.xpath('.//div[2]/a/img/@src').extract_first()
            # print(item)
            yield item
        next_url = response.xpath("//*[@id='content-left']/ul/li[8]/a/@href").extract_first()
        if next_url !=None:
            next_url = "https://www.qiushibaike.com" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )