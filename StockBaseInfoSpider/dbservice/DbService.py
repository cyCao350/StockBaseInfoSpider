# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DbService(object):
    def __init__(self):
        # charset必须设置为utf8，而不能为utf-8
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='111111', db='spiderdb', charset='utf8')
        self.cursor = self.conn.cursor()
        pass

    def close(self):
        if self.cursor:
            self.cursor.close()
            print '---> close cursor'
        if self.conn:
            self.conn.close()
            print '---> close conn'

    # 批量插入多个item
    def process_items(self, items):
        if items:
            for item in items:
                self.insertItem(item)
            self.conn.commit()
        else:
            print '---> process_items error: items is None'

    # 插入单个item
    def process_item(self, item):
        self.insertItem(item)
        self.conn.commit()

    # 没有加异常处理，请自行添加
    # on duplicate key update 这个写法是以表中的唯一索引unique字段为主，去更新其他的字段，兼顾insert和update功能，即没有唯一索引对应的数据，就insert，有就update
    def insertItem(self, item):
        if item:
            sql = "insert into spider_stock_base_info " \
                  "(comp_code, comp_url, comp_name, security_code, exchange, " \
                  "security_name, the_date, whole_capital, circulating_capital, " \
                  "announcement_url) " \
                  "values ('{0}', '{1}', '{2}', '{3}', '{4}', " \
                  "'{5}', '{6}', {7}, {8}, " \
                  "'{9}') " \
                  "on duplicate key update " \
                  "comp_code=values(comp_code), comp_url=values(comp_url), comp_name=values(comp_name), " \
                  "security_name=values(security_name), the_date=values(the_date), whole_capital=values(whole_capital), circulating_capital=values(circulating_capital), " \
                  "announcement_url=values(announcement_url) "
            sql = sql.format(item['compCode'], item['compUrl'], item['compName'], item['securityCode'], item['exchange'],
                             item['securityName'], item['theDate'], item['wholeCapital'], item['circulatingCapital']
                             , item['announcementUrl'])
            self.cursor.execute(sql)

            print '---> insert ', item['securityCode'], item['exchange'], item['securityName'], 'success'
        else:
            print '---> error:item is None, do not insert!'

