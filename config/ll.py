#coding:utf-8
#__author__ =='xuxu'
from config.tidb import cur

sql = 'select * from tb_staff'

try:
    cur.execute(sql)
    results = cur.fetchone()
    print(results)
except:
    print('error')