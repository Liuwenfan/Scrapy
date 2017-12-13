# -*- coding: utf-8 -*-
import codecs


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyfirstPipeline(object):
    def __init__(self):
        self.file = codecs.open("Url.txt", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        for url in item["img_url"]:
            self.file.write("http:" + url + "\n")
        return item

    def close_spider(self, spider):
        self.file.close()
