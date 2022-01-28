import scrapy


class IetfHelloSpider(scrapy.Spider):
    name = 'ietf_hello'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()        
        return {"title" : title}
