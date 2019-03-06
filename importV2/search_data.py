import xlrd
import xm_rdxlpath
import os
import sqlite3
db_filename = 'database.db'
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
def select_table():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    select_sql = "select * from monthtotal"
    result = cursor.execute(select_sql)
    for i in result:
        sbbh = i[0]
        datetime = i[1]
        zt = i[2]
        print("时间:%s,设备编号:%s,设备状态:%s" %(datetime,sbbh,zt))
    cursor.close()
    conn.close()
def select_count_table():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    select_sql = "select count(*) from monthtotal"
    result = cursor.execute(select_sql)
    for i in result:
        print("总量:%s"% i)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    select_table()
    select_count_table()