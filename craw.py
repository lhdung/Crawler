import scrapy
import time
import sys

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # start_urls = ['https://zingnews.vn/cac-kich-ban-chien-thang-qua-5-ky-bau-cu-tong-thong-my-post1141385.html']
        
    def __init__(self, url=None, *args, **kargs):
        super(BlogSpider, self).__init__(*args, **kargs)
        self.start_urls = [url]

    def parse(self, response):
        with open('/app/title.txt', "w") as f:
            f.write(response.css('.the-article-title::text')[0].get())
            f.write('\n')
            f.write(response.css('.the-article-publish::text')[0].get())
            f.write('\n')
            f.write(response.css('.the-article-summary::text')[0].get())
            f.write('\n')
            f.write(response.css('.the-article-body').get())
            f.write('\n')
            f.write(response.css('meta[property="og:image"]').attrib['content'])
