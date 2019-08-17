# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from URY.items import Problem


class ProblemasSpider(scrapy.Spider):
    name = 'problems'

    def __init__(self, start=1001, stop=1005, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ['https://www.urionlinejudge.com.br/repository/UOJ_%s.html' % start]
        self.number = int(start)
        self.stop = int(stop)

    def parse(self, response):
        problems = ItemLoader(item=Problem(), response=response)

        problems.add_css('description', '.description p')
        problems.add_value('number', self.number)
        problems.add_css('output', '.output p')
        problems.add_css('input', '.input p')
        problems.add_css('examples', 'td p')
        problems.add_css('title', 'h1')

        print('\033[32mURI Online Judge | %s\033[m' % self.number)
        yield problems.load_item()

        if self.number < self.stop:
            self.number += 1
            yield scrapy.Request(
                response.urljoin('https://www.urionlinejudge.com.br/repository/UOJ_%s.html' % self.number),
                callback=self.parse)
