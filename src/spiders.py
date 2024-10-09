###############################################################################
### MSDS 436 - Section 55 - Fall '24
### Kevin Geidel
### Research Assignment #1
### scrapy.py - classes and spiders for collecting articles from the web
###############################################################################


import scrapy

# NOTE: Thoughts on abstraction...
# each data source will likely need its own spider class.
# Maybe we can pull a base class out if patterns emerge.
# If the methods can be abstracted then Data source specific
# attributes could be stored in postgres (use class vars for now?)

# TODO: Replace jsonl outputs with an item pipeline to a postgres database!!!!!
# https://medium.com/codelog/store-scrapy-crawled-data-in-postgressql-2da9e62ae272


class CodataSpider(scrapy.Spider):
    ''' A scrapy spider for articles in CODATA's Data Science Journal '''
    SELECTOR_ACCESSOR_ATTR_MAP = {
        # args for scrapy's css method to grab each value
        'type': 'div.cPyXJe::text',
        'title': 'a.wzdQU::text',    
        'authors': 'address.AMuyK::text',
    }
    name = "articles"
    start_urls = [
        "https://datascience.codata.org/articles",
    ]

    def parse(self, response):
        # for datascience.codata.org they use <article> tags around their search records
        for entry in response.css("article"):
            entry_dict = {key: entry.css(self.SELECTOR_ACCESSOR_ATTR_MAP[key]).get() for key in ['type', 'title', 'authors']}
            entry_dict.update(
                {'article_path': entry.css('a.wzdQU').attrib['href']}
            )
            yield entry_dict

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            print("NEXTED!")
            yield response.follow(next_page, self.parse)