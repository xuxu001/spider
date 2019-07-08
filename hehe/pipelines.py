# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HehePipeline(object):
    def open_spider(self,spider):
        self.file = open('item.txt','w',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        try:
            res = dict(item)
            line = res['name']
            tes = res['heh']
            img = res['content']
            self.file.write(line+'\n'+tes+'\n' +img+'\n')
        except:
            pass

        return item
