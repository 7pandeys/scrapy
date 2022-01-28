import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        subheading = response.xpath('//span[@class="subheading"]/text()').getall()
        rfc = response.xpath('//span[@class="rfc-no"]/text()').get()
        author = response.xpath('//span[@class="author-name"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        company = response.xpath('//span[@class="author-company"]/text()').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        text = response.xpath('//div[@class="text"]/text()').get()
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()
        return {"title": title,
                "subheading": subheading,
                "rfc": rfc,
                "author": author,
                "date":date,
                "company": company,
                "address": address,
                "text": text,
                "description": description}
