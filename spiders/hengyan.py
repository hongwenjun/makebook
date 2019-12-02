# -*- coding: utf-8 -*-
import scrapy
from Books.items import BooksItem
from scrapy.http import Request
from scrapy import Selector

class W69shuSpider(scrapy.Spider):
    name = 'hengyan.com'
    allowed_domains = ['hengyan.com']

    # # 书目录   只测试一本书
    def start_requests(self):
    #  #   for num in range(1,5):
        yield scrapy.Request('http://www.hengyan.com/dir/2628.aspx', callback=self.parse_chapter)


    #获取小说章节的URL
    def parse_chapter(self, response):
        chapter_urls = response.xpath('//*[@id="left"]/div[3]/ul/li/a/@href').extract()
        for chapter_url in chapter_urls:
            yield Request('http://www.hengyan.com' + chapter_url, callback=self.parse_content)

    #获取小说名字,章节的名字和内容
    def parse_content(self, response):
        #小说名字
        name = response.xpath('/html/body/div[2]/div[1]/div[1]/p/a[2]/text()').extract_first()
        result = response.text
        #小说章节名字
        chapter_name = response.xpath('/html/body/div[2]/div/div[2]/h2/text()').extract_first()

        # sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()
        # ps = response.xpath('//*[re:test(@id, "contentitem\d+")]/div[3]/p')
        # for p in ps.xpath('.//text()'):
	    #     print (p.extract())

        #小说章节内容
        chapter_content = response.xpath('//*[re:test(@id, "contentitem\d+")]/div[3]/p').extract()
        chapter_content_all = ''
        chapter_content_all.join(chapter_content)
 
        item = BooksItem()
        item['url'] = response.url
        item['name'] = name
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content
        yield item
