from pysql import Pysql as ySql

class OperateSql():
    def __init__(self):
        self.db = ySql({
                "host": "localhost",
                "user": "root",
                "password": "root",
                "db_name": "myscraw"
            })
    def insertData(self, params):
        sql = "INSERT INTO video(title, url, play) VALUES ('{title}', '{url}', '{play}')".format(title=params["title"], url=params["url"], play=params["play"])
        self.db.insertData(sql)
    def closeDb(self):
        self.db.closeConnect()

data_list = []

for i in range(10, 20):
    data_list.append({
      "title": "title-{}".format(i),
      "url": "http://www.baidu.com/pages/{}".format(i),
      "play": "http://www.baidu.com/article?index={}".format(i)
    })

connectSql = OperateSql()
for eachData in data_list:
    connectSql.insertData(eachData)
connectSql.closeDb()
print('插入数据成功!')
