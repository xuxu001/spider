# -*- coding: utf-8 -*-
import scrapy
import string


class CeshiSpider(scrapy.Spider):
    name = 'ceshi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/']
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    # yield scrapy.Request(url=url, headers=header, callback=self.parse)

    def parse(self, response):
        content_list = response.xpath("//div[@id='content-left']/div")
        print(content_list)
        for con in content_list:
            item ={}
            item['body']=con.xpath(".//a/div/span/text()").extract_first()
            item['stater']=con.xpath(".//div[1]/a[2]/h2/text()").extract_first()
            yield item

        last_url = response.xpath("//div[@id='content-left']/ul/li[8]/a/@href").extract_first()
        if last_url !=None:
            next_url = "https://www.qiushibaike.com" + last_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        # print(last_url)
        # b = chr(last_url)
        # print(type(b))
        # # next_url=response.xpath('.//ur/li/a/text()').extract_first()[1:]
        # # next_url = "https://www.qiushibaike.com" + next_url
        # # yield scrapy.Request(
        # #     next_url,
        # #     callback=self.parse
        # # )
        # for a in range(1,b):
        #     next_url = "https://www.qiushibaike.com/text/page/" +a +'/'
        #
        #     yield  scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )


