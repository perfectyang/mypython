import pymysql
# -*- coding: utf-8 -*-
class Pysql(object):

    def __init__(self, arg):
        self.params = arg
        self.connectSql()

    def connectSql(self):
        self.connection = pymysql.connect(host=self.params['host'],
                             user=self.params['user'],
                             password=self.params['password'],
                             db=self.params['db_name'],
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

    def insertData(self, sql):
        # 使用cursor()方法获取操作游标
        cursor = self.connection.cursor()
        db = self.connection
        # # SQL 插入语句
        # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        #          LAST_NAME, AGE, SEX, INCOME)
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 如果发生错误则回滚
           db.rollback()
    def closeConnect(self):
        self.connection.close()
