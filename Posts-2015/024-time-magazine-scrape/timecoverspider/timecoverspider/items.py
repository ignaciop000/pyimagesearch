# import the necessary packages
import scrapy

class MagazineCover(scrapy.Item):
	title = scrapy.Field()
	pubDate = scrapy.Field()
	file_urls = scrapy.Field()
	files = scrapy.Field()