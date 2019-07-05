# -*- coding: utf-8 -*-
import scrapy


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    def start_requests(self):

        url = 'https://www.qiushibaike.com/text/page/'
        header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        yield scrapy.Request(url=url,headers=header,callback=self.parse)
    def parse(self, response):
        # result= response.xpath('//*[@id="content-left"]/div/a/div/span/text()').extract()
        # print(result)
        #分组
        li_list = response.xpath('//*[@id="content-left"]/div')
        for li in li_list:
            item = {}
            item['body']=li.xpath('.//a/div/span/text()').extract_first()
            yield item


