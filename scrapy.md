## scrapy 爬虫程序安装
```
apt install python3-pip
pip3 install scrapy

scrapy startproject Books                  # 建立爬虫项目
cd Books
scrapy genspider  BooksA  <<爬虫英文名>>   # 建立爬虫

```
------------------

### 修改爬虫程序相关2个文件

- vim  ./Books/spiders/BooksA.py    # 更新蜘蛛程序

- vim  ./Books/items.py

```python
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

```

### 测试蜘蛛爬虫程序，按 CTRL-C 退出 
scrapy crawl <<爬虫英文名>>

### 储存数据 爬虫名  -o 保存文件，支持 json xml csv jl 格式
scrapy crawl <<爬虫英文名>> -o book.csv


### 爬虫框架目录结构
```
root@kvm-VirMach:~/Books$ du -ah
4.0K    ./Books/middlewares.py        # 下载器中间件是在引擎及下载器之间的特定钩子 (specific hook)是用来让其他程序连接scrapy的
4.0K    ./Books/pipelines.py          # 定义数据导出类，用于数据导出
4.0K    ./Books/spiders/BooksA.py     # 自己编码的蜘蛛程序
4.0K    ./Books/spiders/__pycache__/__init__.cpython-35.pyc
4.0K    ./Books/spiders/__pycache__/BooksA.cpython-35.pyc
12K     ./Books/spiders/__pycache__
4.0K    ./Books/spiders/__init__.py
24K     ./Books/spiders               # 爬虫目录，用于放置各种爬虫类文件
4.0K    ./Books/__pycache__/settings.cpython-35.pyc
4.0K    ./Books/__pycache__/items.cpython-35.pyc
4.0K    ./Books/__pycache__/__init__.cpython-35.pyc
16K     ./Books/__pycache__
0       ./Books/__init__.py
4.0K    ./Books/items.py            # 定义数据条目的定义
4.0K    ./Books/settings.py         # 工程设置文件
60K     ./Books                     # 工程模块
4.0K    ./scrapy.cfg                # 开发配置文件

```

### 参考文档和教程
https://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_python_007_scrapy01.html

```
参考 scrapyhub 教程
shub login
shub deplpy xxxx
```
