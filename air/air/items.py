# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FlightItem(scrapy.Item):
    depCityName = scrapy.Field()    # 起飞城市
    arrCityName = scrapy.Field()    # 着陆城市

    depTime = scrapy.Field()    #起飞时间
    arrTime = scrapy.Field()    #着陆时间

    price = scrapy.Field()      #价格
    TotalPrice= scrapy.Field()  #总价

class AirItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
