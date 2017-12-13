# -*- coding: utf-8 -*-
import scrapy
from myfirst.items import MyfirstItem
from scrapy.http import Request


class TestSpider(scrapy.Spider):
    name = 'test'
    part_url = 'https://www.qiushibaike.com/imgrank/'
    page = 'page/'

    def start_requests(self):
        yield self.make_requests_from_url(self.part_url)

    def parse(self, response):
        item = MyfirstItem()
        item["img_url"] = response.xpath("//div[@class='thumb']/a/img/@src").extract()
        yield item
        for i in range(2, 13, 1):
            url = self.part_url + self.page + str(i) + "/"
            yield Request(url, callback=self.parse)
