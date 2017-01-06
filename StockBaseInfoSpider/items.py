# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class StockbaseinfospiderItem(Item):
    # 公司代码
    compCode = Field()
    # 公司详情页url
    compUrl = Field()
    # 公司简称
    compName = Field()
    # 证券代码
    securityCode = Field()
    # 交易所代码
    exchange = Field()
    # 证券简称
    securityName = Field()
    # 上市日期
    theDate = Field()
    # 总股本
    wholeCapital = Field()
    # 流通股本
    circulatingCapital = Field()
    # 公司公告列表页url
    announcementUrl = Field()
