import scrapy

from tutorial.items import TutorialItem


class TutorialSpider( scrapy.Spider ):

    # Identifies the spider. Must be unique to any set of spiders!
    name = 'tutorial'

    allowed_domains = [ 'dmoz.org' ]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse( self, response ):

        for sel in response.xpath( '//ul/li' ):
            item = TutorialItem()
            item['title'] = [x.strip() for x in sel.xpath( 'a/text()' ).extract()]
            item['link']  = [x.strip() for x in sel.xpath( 'a/@href' ).extract()]
            item['desc']  = [x.strip() for x in sel.xpath( 'text()' ).extract()]
            yield item
