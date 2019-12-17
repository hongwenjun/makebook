```
https://www.youtube.com/srgb18/videos

https://www.youtube.com/channel/UCupRwki_4n87nrwP0GIBUXA/videos

file = 'my.html'
with open(file, 'wb') as f:
    f.write(response.body)
  
xp = '/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div/div/div/div/ul/li[2]/ul/li/div/div/div/h3/a' 
myvods =  response.xpath( xp ).getall()
urls = response.xpath( xp + '/@href' ).getall()


response.xpath(xp)

```

```
import scrapy

class YoutebeSpider(scrapy.Spider):
    name = "youtebe"
    allowed_domains = ["youtube.com"]
    start_urls = [
        "https://www.youtube.com/srgb18/videos",
    ]

    def parse(self, response):
        filename = 'youtebe.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        # xp = '/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div/div/div/div/ul/li[2]/ul/li/div/div/div/h3/a'

        xp = '//*[@id="channels-browse-content-grid"]/li/div/div[1]/div[2]/h3/a'

        myvods =  response.xpath( xp + '/text()'  ).getall()
        urls = response.xpath( xp + '/@href' ).getall()
        
        for i in range(len(myvods)):
            print( myvods[i]+ '   https://www.youtube.com'  + urls[i])
    ```
