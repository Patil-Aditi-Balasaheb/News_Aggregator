import scrapy
from ..items import TopcrawlerItem
from news.models import TopHeadline
from topcrawler.spiders import top_spider
from topcrawler import pipelines

class TopSpider(scrapy.Spider):
	name = "top"
	start_urls = [
		'https://www.hindustantimes.com/'
	]

	def parse(self, response):
		div_all_news = response.xpath("//div[@class='cartHolder listView']")
		i=0
		for some in div_all_news:
			items = TopcrawlerItem()
			title = some.xpath("//h3[@class='hdg3']/a/text()")[i].extract()
			link = "https://www.hindustantimes.com" + some.xpath("//h3[@class='hdg3']/a/@href")[i].extract()
			img = some.xpath("//figure/span/a/img/@src")[i].extract()
			i+=1 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Hindustan Times'
			yield items
			#if i==10:
			#	break
