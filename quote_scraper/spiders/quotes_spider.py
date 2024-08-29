# quote_scraper/quotes_scraper/spiders/quotes_spider.py

import scrapy
from scrapy.http import FormRequest
from ..items import QuoteScraperItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/login"]

    def parse(self, response):
        # Extract the CSRF token (if necessary)
        csrf_token = response.css("input[name='csrf_token']::attr(value)").get()

        # Prepare the form data
        return FormRequest.from_response(
            response,
            formdata={
                "username": "your_username",
                "password": "your_password",
                "csrf_token": csrf_token  # Include if the form uses a CSRF token
            },
            callback=self.parse_quotes
        )

    def parse_quotes(self, response):

        self.logger.info("Successfully reached quotes page")
        # Scrape the quotes after logging in
        for quote in response.css("div.quote"):
            item = QuoteScraperItem()
            item['title'] = quote.css("span.text::text").get()
            item['author'] = quote.css("small.author::text").get()
            item['tags'] = quote.css("a.tag::text").getall()
            yield item

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            self.logger.info(f"Following pagination link: {next_page}")
            yield response.follow(next_page, self.parse_quotes)
