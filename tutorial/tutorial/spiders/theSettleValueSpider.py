#coding:utf-8

import scrapy
from tutorial.items import SettleValueItem
from tutorial.spiders.theSettleValueGetUrl import GetSettleUrl
import urllib.parse

# 获取清算后的基金净值爬虫
class theSettleValueSpider(scrapy.Spider):
    name = 'theSettleValue'
    allowed_domains = []
    custom_settings = {
    	'ITEM_PIPELINES':{'tutorial.pipelines.SettleMysqlPipeline': 301},
    }

    # 获取天天基金的请求url
    start_urls = GetSettleUrl.getTtjjFundUrl(GetSettleUrl)

    # 解析天天基金的数据
    def parse(self, response):
        print(response.url)
        # 处理获取到的数据      
        params = urllib.parse.parse_qs(urllib.parse.urlparse(response.url).query)
        # 将当前页的数据存储
        for tr in response.xpath("//tbody//tr"):
            # print(tr)
            item = SettleValueItem()
            item['code'] = params['code'][0]
            item['date'] = tr.xpath("./td[1]/text()").extract_first()
            item['unitValue'] = tr.xpath("./td[2]/text()").extract_first()
            item['totalValue'] =  tr.xpath("./td[3]/text()").extract_first()
            item['riseRate'] =  tr.xpath('substring-before(./td[4]/text(), "%")').extract_first()
            print(item)
            yield item
