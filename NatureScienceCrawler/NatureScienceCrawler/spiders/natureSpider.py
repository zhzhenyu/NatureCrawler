import scrapy

'''
This crawler aims to extract URLs of articles published in nature.com
'''

class QuotesSpider(scrapy.Spider):
    name = "nature"
    start_urls = [
        'https://www.nature.com/nature/articles?type=article',
    ]


    def parse(self, response):
        for url in response.css('body div.content div div div div div h3 a::attr(href)').getall():
            yield {
                    'URL': 'https://www.nature.com' + url,
            }

        next_page = response.css('body div.position-relative.z-index-1 div.container.cleared.container-type-pagination div nav ol li a::attr(href)').getall()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)