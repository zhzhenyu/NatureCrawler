import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        f = open('URLs.json')
        data = json.load(f)
        start_URLs = []
        for entry in data:
            start_URLs.append(entry['URL'])

        for url in start_URLs:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        subjects = response.css('[class="c-article-subject-list__subject"]')
        subjectList = []
        for subject in subjects:
            subjectList.append(subject.css('a::text').get())

        yield {
            'title': response.css('body div.u-container.u-mt-32.u-mb-32.u-clearfix main article div header h1::text').get(),
            'author': response.css('a#corresp-c1::text').get(),
            'subject': subjectList
        }
