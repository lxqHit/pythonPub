#coding:utf-8

import scrapy
from tutorial.spiders.theNowValueGetUrl import GetNowValueUrl
from tutorial.items import NowValueItem

class theNowValueSpider(scrapy.Spider):
    name = 'theNowValue'
    allowed_domains = []
    custom_settings = {
    	'ITEM_PIPELINES':{'tutorial.pipelines.NowMysqlPipeline': 302},
    }

    # 获取实时估值的请求url
    start_urls = GetNowValueUrl.getGzFundUrl(GetNowValueUrl)

    # 解析实时估值的数据
    def parse(self, response):
        print(response.url)
        # 处理获取到的数据  
        # 将当前页的数据存储
        item = NowValueItem()
        item['code'] = response.xpath('''substring-before(substring-after(//body, 'fundcode":"'), '","name')''').extract_first()
        item['nowValue'] = response.xpath('''substring-before(substring-after(//body, 'gsz":"'), '","gszzl')''').extract_first()
        item['time'] = response.xpath('''substring-before(substring-after(//body, 'gztime":"'), '"});')''').extract_first()
        item['riseRate'] = response.xpath('''substring-before(substring-after(//body, 'gszzl":"'), '","gztime')''').extract_first()
        print(item)
        yield item
            
            