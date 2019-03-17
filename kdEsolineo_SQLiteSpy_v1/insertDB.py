# -*- coding: utf-8 -*-
import os
import sqlite3
import esqueryInfo

db_filename = 'database.db'
#db_is_new = not os.path.exists(db_filename)
def sqlite3_db_create():
    try:
        if not os.path.exists(db_filename):
            conn = sqlite3.connect(db_filename)
            c = conn.cursor()
            c.execute('''CREATE TABLE test(number1 varchar(200),name varchar(200),message varchar(200));''')
            conn.commit()
            conn.close()
        else:
            pass
    except Exception as e:
        print(e)

def insertDB():
    del_table()
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    es = esqueryInfo.ElasticSearchMrg()
    queryList = esqueryInfo.LoadConf()
    #print(queryList[0])
    esdata = es.searchInfo(queryList[0])
    #print(esdata)
    for line_kk in esdata:
        #print(kk['_source'])
        line = line_kk['_source']
        number1 = line['number1']
        name = str(line['name'])
        message = str(line['message'])
        sql = "insert into test (number1,name,message) values ('%s','%s','%s')" %(number1,name,message)
        #print(number1,name,message)
        #return number1, name, message
        print(sql)
        c.execute(sql)
        conn.commit()
    conn.close()
    conn.close()

def del_table():
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    del_sql = "delete from test"
    c.execute(del_sql)
    conn.commit()
    conn.close()
    conn.close()



