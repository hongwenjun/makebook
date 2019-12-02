import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"                   # 蜘蛛爬虫名
    allowed_domains = ["srgb.work"]  #  允许的域

    # start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 
    # 后续的URL则从初始的URL获取到的数据中提取。
    start_urls = [
        "https://www.srgb.work/tags/CodeBlocks/",
        "https://www.srgb.work/2018/08/03/code/psdda/"
    ]


    # parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'   # URLq 切割获取 文件名
        with open(filename, 'wb') as f:                    # 保存 返回的数据(response data) 到文件
            f.write(response.body)                         # html.body 写文件

            # 使用选择器(selectors): 使用 Scrapy shell (提供交互测试)和位于Scrapy文档服务器的一个样例页面，来解释如何使用选择器：
            # https://scrapy-chs.readthedocs.io/zh_CN/1.0/topics/selectors.html

            # scrapy shell https://www.srgb.work/tags/CodeBlocks/  
            
            cb_urls = response.xpath('//*[@id="main"]/section/div[2]/article/div/header/h1/a/@href').extract()
            cb_titles = response.xpath('/html/body/div/div/div/section/section/div[2]/article/div/header/h1/a/text()').extract()

            for url in cb_urls:
                print(url)
            for title in cb_titles:
                print(title)

            # 提取真实的原文数据，调用 .extract() 方法; 提取到第一个匹配到的元素, 必须调用 .extract_first()
            url = response.xpath('/html/body/div/div/div/section/section/div[2]/article/div/header/h1/a/@href').extract_first()
            print(url)

            # 另外还有一个糅合了 .extract_first() 与 .re() 的函数 .re_first() . 使用该函数可以提取第一个匹配到的字符串:
            # >>> response.xpath('//a[contains(@href, "image")]/text()').re_first(r'Name:\s*(.*)')
            # u'My image 1'

            # 结合正则表达式使用选择器(selectors)
            # response.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
            # 正则表达式  在XPath的 starts-with() 或 contains() 无法满足需求时， test() 函数可以非常有用
            # sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract()
            # ps = response.xpath('//*[re:test(@id, "contentitem\d+")]/div[3]/p')
            # for p in ps.xpath('.//text()'):
            #     print (p.extract())