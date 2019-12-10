# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # pass

    url = scrapy.Field()  # 小说链接
    name = scrapy.Field() # 小说名字
    chapter_name = scrapy.Field()   # 小说章节名字
    chapter_content = scrapy.Field()  # 小说章节内容


