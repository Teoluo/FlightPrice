# -*- coding: utf-8 -*-
import scrapy
import json
from .. import items

class FlypigSpider(scrapy.Spider):
    name = 'flypig'
    allowed_domains = ['sjipiao.fliggy.com']
    #start_urls = ['https://sjipiao.fliggy.com/searchow/search.htm?_ksTS=1551842301537_172&callback=jsonp173&tripType=0&depCity=CTU&depCityName=%E6%88%90%E9%83%BD&arrCity=FOC&arrCityName=%E7%A6%8F%E5%B7%9E&depDate=2019-03-08&searchSource=99&searchBy=1280&sKey=&qid=&needMemberPrice=true&_input_charset=utf-8&ua=090%23qCQX8TX2X2OXPXi0XXXXXQkOOoRlTUjABlToI6hiAGB3zzx4hY5G%2B%2FiOIrU9HGGh3vQXiPR22a4kXvXuLWQ5HfxkH4QXaPjPiUgXDzoE%2F4QXU6hnXXa3HoQCh9T4jx73OAfeG2XPHYVyrFhnLXj3HoDYh9k4aP73IzjBXvXzxDkjIEBKgF4NKjBfFGqF1X4s6xDiXX0XTxRwvZPtXvXQ0ZsNLv%3D%3D&openCb=false']

    def start_requests(self):
        cookies="cna=FuaSFDaMHnYCAbaWby+df99H; hng=CN%7Czh-CN%7CCNY%7C156; lid=teoteo10; UM_distinctid=1694c210ced0-00b9b7f1f589-3d644701-1fa400-1694c210cee51b; uss=""; enc=1Pj%2BgzlnFUSdfFq18mo1HjfDxxLi3X%2FcwAZkhapDUWnJ%2B8kG0EfwzK71hFT07OmZDJlsNAJ5UG6A2KuX3ApHLw%3D%3D; t=69c2773e3736a63aa878863d9d5583e5; tracknick=teoteo10; _tb_token_=QMhJf0pjTxFcfvtwaJvS; cookie2=11e08a51502954666882d277f97181cd; CNZZDATA30066717=cnzz_eid%3D1475742120-1551755360-https%253A%252F%252Fwww.fliggy.com%252F%26ntime%3D1551838019; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=UtASsssmeW6lpyd%2BB%2B3t&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bsW48yBGA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEvwaG1ou1GzMHE%3D&id2=Uoe8izYyP0CEOA%3D%3D&nk2=F5NEvZp5mCs%3D&lg2=URm48syIIVrSKA%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=1681717150; lgc=teoteo10; cookie1=VWZ4FguLLZya6FhYHiiwZ%2Fc4U%2Bc4lBe3XE1u7WNozSc%3D; login=true; cookie17=Uoe8izYyP0CEOA%3D%3D; _nk_=teoteo10; csg=7bd94f2a; skt=865ac96efdfb70c9; isg=BO3tv9v7TTMiayldY7SuG7dm_Imn4uZ5DHt6Qy_yKQTzpg1Y95ox7Dt2lDrlJjnU"
        cookies = {item.split("=")[0]: item.split("=")[1] for item in cookies.split("; ")}
        for i in range(7,30):
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
        for item in response_dic["data"]["flight"]:
            totalPrice = item["buildPrice"]+item["cabin"]["price"]
            yield items.FlightItem(depCityName="CD",arrCityName="FZ",depTime=item["depTime"],arrTime=item["arrTime"],price=item["cabin"]["price"],TotalPrice=totalPrice)