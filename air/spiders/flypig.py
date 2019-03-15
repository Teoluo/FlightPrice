# -*- coding: utf-8 -*-
import scrapy
import json
from .. import items

class FlypigSpider(scrapy.Spider):
    name = 'flypig'
    allowed_domains = ['sjipiao.fliggy.com']
    #start_urls = ['https://sjipiao.fliggy.com/searchow/search.htm?_ksTS=1551842301537_172&callback=jsonp173&tripType=0&depCity=CTU&depCityName=%E6%88%90%E9%83%BD&arrCity=FOC&arrCityName=%E7%A6%8F%E5%B7%9E&depDate=2019-03-08&searchSource=99&searchBy=1280&sKey=&qid=&needMemberPrice=true&_input_charset=utf-8&ua=090%23qCQX8TX2X2OXPXi0XXXXXQkOOoRlTUjABlToI6hiAGB3zzx4hY5G%2B%2FiOIrU9HGGh3vQXiPR22a4kXvXuLWQ5HfxkH4QXaPjPiUgXDzoE%2F4QXU6hnXXa3HoQCh9T4jx73OAfeG2XPHYVyrFhnLXj3HoDYh9k4aP73IzjBXvXzxDkjIEBKgF4NKjBfFGqF1X4s6xDiXX0XTxRwvZPtXvXQ0ZsNLv%3D%3D&openCb=false']

    def start_requests(self):
        cookies="cna=FuaSFDaMHnYCAbaWby+df99H; hng=CN%7Czh-CN%7CCNY%7C156; lid=teoteo10; UM_distinctid=1694c210ced0-00b9b7f1f589-3d644701-1fa400-1694c210cee51b; uss=""; enc=1Pj%2BgzlnFUSdfFq18mo1HjfDxxLi3X%2FcwAZkhapDUWnJ%2B8kG0EfwzK71hFT07OmZDJlsNAJ5UG6A2KuX3ApHLw%3D%3D; uc1=cookie14=UoTZ5iFytzXlFg%3D%3D; t=69c2773e3736a63aa878863d9d5583e5; tracknick=teoteo10; _tb_token_=e1e87b33e5f55; cookie2=1e8e9c9644f96d57103d47907ff1bf2c; CNZZDATA30066717=cnzz_eid%3D1475742120-1551755360-https%253A%252F%252Fwww.fliggy.com%252F%26ntime%3D1552470950; isg=BLq60yJbsr0BJT6kCDWhkpwXC-Acw_kgF-pNWsSzIM0Yt1vxrPqyVP6FBwPOJ7bd; l=bBMJpC-HvXNp1J1sBOCiCuIRtPbtKIRfguPRw0cXi_5BV6Y_Mw_Ol1E6rFv6Vj5POqLB4dJnHQeTieDT-y8f."
        cookies = {item.split("=")[0]: item.split("=")[1] for item in cookies.split("; ")}
        for i in range(13,30):
            depDate = "depDate=2019-03-" + str(i)
            url = 'https://sjipiao.fliggy.com/searchow/search.htm?_ksTS=1551842301537_172&callback=jsonp173&tripType=0&depCity=CTU&depCityName=%E6%88%90%E9%83%BD&arrCity=FOC&arrCityName=%E7%A6%8F%E5%B7%9E&'+depDate+'&searchSource=99&searchBy=1280&sKey=&qid=&needMemberPrice=true&_input_charset=utf-8&ua=090%23qCQX8TX2X2OXPXi0XXXXXQkOOoRlTUjABlToI6hiAGB3zzx4hY5G%2B%2FiOIrU9HGGh3vQXiPR22a4kXvXuLWQ5HfxkH4QXaPjPiUgXDzoE%2F4QXU6hnXXa3HoQCh9T4jx73OAfeG2XPHYVyrFhnLXj3HoDYh9k4aP73IzjBXvXzxDkjIEBKgF4NKjBfFGqF1X4s6xDiXX0XTxRwvZPtXvXQ0ZsNLv%3D%3D&openCb=false'
            #print(url)
            yield scrapy.Request(
                url,
                cookies=cookies,
                callback=self.parse
            )

    def parse(self, response):
        response_str=response.body_as_unicode()
        response_str=response_str[response_str.index("(")+1 : len(response_str)-3]
        response_dic=json.loads(response_str)
        print(response_dic)
        for item in response_dic["data"]["flight"]:
            totalPrice = item["buildPrice"]+item["cabin"]["price"]

            depYear = item["depTime"].split(" ")[0].split("-")[0]
            depMouth = item["depTime"].split(" ")[0].split("-")[1]
            depDay = item["depTime"].split(" ")[0].split("-")[2]
            depTime = item["depTime"].split(" ")[1]

            arrYear = item["arrTime"].split(" ")[0].split("-")[0]
            arrMouth = item["arrTime"].split(" ")[0].split("-")[1]
            arrDay = item["arrTime"].split(" ")[0].split("-")[2]
            arrTime = item["arrTime"].split(" ")[1]

            yield items.FlightItem(
                depCityName="CD",
                arrCityName="FZ",

                depYear=depYear,
                depMouth=depMouth,
                depDay=depDay,
                depTime=depTime,

                arrYear=arrYear,
                arrMouth=arrMouth,
                arrDay=arrDay,
                arrTime=arrTime,

                price=item["cabin"]["price"],
                TotalPrice=totalPrice
            )