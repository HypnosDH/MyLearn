# -*- coding: utf-8 -*-
import scrapy


class BooksCrawlerSpider(scrapy.Spider):
    name = 'books_crawler'
    # allowed_domains = ['https://www.books.com.tw/web/books_nbtopm_19/']
    start_urls = ['https://www.books.com.tw/web/books_nbtopm_19/']

    def parse(self, response):
        for book in response.css("div.item"):  #div.item = <div class="item">
            name = book.css("div.msg h4 a::text").get() #<div class="msg"><h4><a href=""=>text</a></h4></div>
            url = book.css("div.msg h4 a::attr(href)").get() #<div class="msg"><h4><a href=""=>text</a></h4></div>
            price = book.css("div.price_box ul.price li.set2 strong::text").getall()

            yield {
                "book name" : name,
                "Web Url" : url,
                "Price" : price[1],
                "Discount" : price[0]
            }

