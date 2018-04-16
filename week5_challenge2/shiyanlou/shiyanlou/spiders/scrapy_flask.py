import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from shiyanlou.items import ShiyanlouItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
	name = 'scrapy_flask';
	allowed_domains = ['falsk.pocoo.org']
	start_urls = ["http://flask.pocoo.org/docs/0.12/"]
	
	pagelink =  LinkExtractor(allow=(r'http://flask.pocoo.org/docs/0.12/.*'))
	rules=[Rule(pagelink,callback='parse_page',follow=True),]
	
def parse_page(self,response):
	item = PageItem()
	
	item['url']=str(response)
	texts=[]
	texts=response.xpath('string(//div[@class="section"])').extract()
	item['text']=re.sub(r'[\s]+'," ",texts[0])
	#print(item)
	yield item
	