# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Delay downloads to be nice to the Internet Archive
DOWNLOAD_DELAY = 0.25

# Enable the image pipeline
# See for more info:
# http://doc.scrapy.org/en/latest/topics/images.html#topics-images-enabling
ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

# Also have an example of thumbnail generation
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

IMAGES_STORE = '/tmp/scrapy'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
