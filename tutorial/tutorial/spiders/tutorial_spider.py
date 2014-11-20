import scrapy

from scrapy.http import Request
from tutorial.items import TutorialItem, CoverArtItem


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


class TutorialImageSpider( scrapy.Spider ):
    '''
        A little more complex spider example which goes through the Internet
        Archive's recently added cover art section and downloads them.
    '''
    name = 'coverart'

    allowed_domains = [ 'archive.org' ]

    # Recently added cover art
    start_urls = [
        "https://archive.org/search.php?query=collection%3Acoverartarchive&sort=-publicdate"
    ]

    def parse( self, response ):
        '''
            Parse the recently added page and grab all the detail page links as the
            first step to the cover art.
        '''
        for sel in response.xpath( "//a[contains(@class,'titleLink')]/@href" ):

            # Yield a new request to the cover art detail page
            yield Request( url='https://archive.org{}'.format( sel.extract() ),
                           callback=self.parse_detail )

    def parse_detail( self, response ):
        '''
            Parse the cover art detail page grabbing:
                - Artist name
                - Album title
                - Album art image
        '''

        item = CoverArtItem()
        item[ 'title' ]      = response.xpath( '//span[@class="x-archive-meta-title"]/text()' ).extract()
        item[ 'artist' ]     = response.xpath( '//h1/span[1]/text()' ).extract()
        item[ 'image_urls' ] = [ 'https://archive.org{}'.format( x )
                                 for x in response.xpath( "//p[@id='dl']/a[1]/@href")
                                                  .extract() ]
        yield item
