# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import re
import json

class ShiyanlouPipeline(object):
	def process_item(self, item, spider):
		item['url'] = item['url'].split(" ")[1][:-1]
		data = json.dumps(dict(item))
		self.redis.lpush('flask_doc::item',data)
		
		return item

	def open_spider(self,spider):
		self.redis=redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
		