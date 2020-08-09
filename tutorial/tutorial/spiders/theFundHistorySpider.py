#coding:utf-8

import scrapy
import urllib.parse
from tutorial.items import HistoryValueItem
from tutorial.spiders.theFundHistoryGetUrl import GetUrl

# 获取指定基金的历史数据爬虫
class theFundHistorySpider(scrapy.Spider):
    name = 'theFundHistory'
    allowed_domains = []
    custom_settings = {
    	'ITEM_PIPELINES':{'tutorial.pipelines.HistoryMysqlPipeline': 300},
    }

    # 请求url(天弘)
    # start_urls = GetUrl.getThFundUrl(GetUrl)
    # 请求url(广发)
    # start_urls = GetUrl.getGfFundUrl(GetUrl)
    # 请求url(其他)
    start_urls = GetUrl.getElseFundUrl(GetUrl)
    # 请求url(新增)
    # start_urls = GetUrl.getAddNewFundUrl(GetUrl)

    def parse(self, response):
        print(response.url)
        # 处理获取到的数据      
        params = urllib.parse.parse_qs(urllib.parse.urlparse(response.url).query)
        # print(params['code'])
        # 将当前页的数据存储
        for tr in response.xpath("//tbody//tr"):
            # print(tr)
            item = HistoryValueItem()
            item['code'] = params['code'][0]
            item['date'] = tr.xpath("./td[1]/text()").extract_first()
            item['unitValue'] = tr.xpath("./td[2]/text()").extract_first()
            item['totalValue'] =  tr.xpath("./td[3]/text()").extract_first()
            item['riseRate'] =  tr.xpath('substring-before(./td[4]/text(), "%")').extract_first()
            print(item)
            yield item
        
        # 计算还有没有下一页
        # 网页中的最大页码
        print(response.xpath('substring-before(substring-after(//body, "pages:"), ",curpage")').extract_first())
        maxPage = response.xpath('substring-before(substring-after(//body, "pages:"), ",curpage")').extract_first()
        # 目前请求到第几页
        myPage = params['page'][0]
        print(myPage)
        # 判断没到最后一页则继续请求
        if int(myPage) < int(maxPage):
            # 拼接请求url
            orgUrl = "http://fund.eastmoney.com/f10/F10DataApi.aspx"
            next_page = str(int(myPage) + 1)
            # print(params)
            next_params = {'type': 'lsjz', 'code': params['code'][0], 'page': next_page, 'per': 20,\
            'sdate': params['sdate'][0], 'edate': params['edate'][0]}
            query_string = urllib.parse.urlencode(next_params)
            # print(query_string)
            next_url = orgUrl + '?' + query_string
            print(next_url)
            yield scrapy.Request(next_url, callback = self.parse)