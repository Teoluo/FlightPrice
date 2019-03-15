# FlightPrice V1.1

该爬虫爬取**飞猪**2019-3-7 到 2019-3-30所有的从从成都到福州航班信息

## 模拟登陆
使用cookie模拟登陆

## 获取数据
获取ＪＳＯＮ动态数据

## 保留信息
只提取起飞城市、到达城市，起飞时间、到达时间，机票价格，以及加上基建的总价

## 数据展示
通过Tableau进行数据展示
筛选条件：Totalｐｒｉｃｅ从最低价格－８００
通过颜色的深浅（越深价格越低）以及柱形图的高低（越低价格越低）来判断最低价格，以及观察价格的走势
 ![image](https://github.com/Teoluo/FlightPrice/blob/master/screenshots/1.png)

## Update
2019/3/13  针对数据提取进行改进
