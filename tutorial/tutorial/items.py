# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    ''' Tutorial item '''
    title = scrapy.Field()
    link  = scrapy.Field()
    desc  = scrapy.Field()
