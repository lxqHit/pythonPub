# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 基金历史净值数据item
class HistoryValueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    date = scrapy.Field()
    unitValue = scrapy.Field()
    totalValue = scrapy.Field()
    riseRate = scrapy.Field()

# 基金结算净值数据item
class SettleValueItem(scrapy.Item):
    code = scrapy.Field()
    date = scrapy.Field()
    unitValue = scrapy.Field()
    totalValue = scrapy.Field()
    riseRate = scrapy.Field()

# 基金估值的数据item
class NowValueItem(scrapy.Item):
    code = scrapy.Field()
    nowValue = scrapy.Field()
    time = scrapy.Field()
    riseRate = scrapy.Field()