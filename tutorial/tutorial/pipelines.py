# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi

# 基金历史数据保存，使用异步存储
class HistoryMysqlPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql',**adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        if spider.name == "theFundHistory":
            # print(item)
            query = self.dbpool.runInteraction(self.do_insert,item)  # 指定操作方法和操作数据
            # 添加异常处理
            query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self,cursor,item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
        insert into fund_value_history(code, fund_date, value, total_value, rise_rate) VALUES(%s,%s,%s,%s,%s)
                    """
        cursor.execute(insert_sql,(pymysql.escape_string(item['code']), pymysql.escape_string(item['date']),\
        pymysql.escape_string(item['unitValue']), pymysql.escape_string(item['totalValue']), pymysql.escape_string(item['riseRate'])))

    def handle_error(self,failure):
        if failure:
            # 打印错误信息
            print(failure)

# 基金结算的数据存储，同步处理
class SettleMysqlPipeline(object):
    """
    同步操作
    """
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(
           host = 'localhost',  
           port = 3307,
           user = 'root',
           password = 'xq123l',
           db = 'funddb',
           charset = 'utf8'      
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, myitem, spider):
        if spider.name == "theSettleValue":
            # 因为建立了日期和代码的联合唯一索引，可以直接保存
            insert_sql = """
            insert into fund_value_history(code, fund_date, value, total_value, rise_rate) VALUES(%s,%s,%s,%s,%s)
                    """
            # 执行插入数据到数据库操作
            # print(myitem)
            self.cursor.execute(insert_sql,(myitem['code'], myitem['date'],myitem['unitValue'], myitem['totalValue'], myitem['riseRate']))
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
 
    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

# 基金实时估值的数据存储，同步处理
class NowMysqlPipeline(object):
    """
    同步操作
    """
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(
           host = 'localhost',  
           port = 3307,
           user = 'root',
           password = 'xq123l',
           db = 'funddb',
           charset = 'utf8'      
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name == "theNowValue":
            # 查询是否有历史估值记录
            select_sql = """
            select count(1) from fund_value_now where code = %s
                    """
            self.cursor.execute(select_sql, (item['code']))
            results = self.cursor.fetchall()
            print(results)
            if results != None:
                # 假如数据库不存在基金对应记录
                if int(results[0][0]) == 0:
                    insert_sql = """
                    insert into fund_value_now(code, value_now, now_time, update_time, rise_rate) VALUES(%s,%s,%s,now(),%s)
                            """
                    # 执行插入数据到数据库操作
                    self.cursor.execute(insert_sql,(item['code'], item['nowValue'],item['time'], item['riseRate']))
                    # 提交，不进行提交无法保存到数据库
                    self.conn.commit()
                # 假如存在记录
                if int(results[0][0]) > 0:
                    update_sql = """
                    update fund_value_now set value_now = %s, now_time = %s, update_time = now(), rise_rate = %s where code = %s
                            """
                    # 执行更新数据到数据库操作
                    self.cursor.execute(update_sql,(item['nowValue'], item['time'], item['riseRate'], item['code']))
                    # 提交，不进行提交无法保存到数据库
                    self.conn.commit()
            
 
    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()