import pymysql

db = pymysql.connect(host="localhost",user='root',password='12345678',charset='utf8')
print(db)