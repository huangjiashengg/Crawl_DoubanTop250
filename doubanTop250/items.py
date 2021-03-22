# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    poster_links = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    type = scrapy.Field()
    score = scrapy.Field()
    Num_of_appraisers = scrapy.Field()
    quote = scrapy.Field()
    # name = scrapy.Field()
    # img = scrapy.Field()
    # index = scrapy.Field()
    # score = scrapy.Field()
    # author = scrapy.Field()
    # intr = scrapy.Field()
    pass


