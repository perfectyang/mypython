import csv
import os

gameName = []
with open("./1000.csv", "r",  newline='',encoding="gb18030") as csvfile:
     #读取csv文件，返回的是迭代类型
     read = csv.reader(csvfile)
     for inx, item in enumerate(read):
         print('item', item)
         print('inx', inx)
         if item[0] and item[0] != '产品名称':
             # obj = {
             #   "text": item[0],
             #   "abbr": item[1],
             #   "nickName": item[2]
             # }
             gameName.append({
               "text": item[0],
               "abbr": item[1],
               "nickName": item[2]
             })
             print(item)
     print('gameName', gameName)
     print(len(gameName))
