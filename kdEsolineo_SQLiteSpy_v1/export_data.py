# -*- coding: utf-8 -*-
import sqlite3
from openpyxl import Workbook
#wb = Workbook()
db_filename = 'database.db'
#db_is_new = not os.path.exists(db_filename)
table_name = "卡口在线率.xls"
sheet_name = "1月份"
select_sql = "select * from test order by number1"
def excel_export(wb):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    create_wb(wb,table_name)
    ws = wb.create_sheet(title=sheet_name, index=0)
    c.execute(select_sql)
    #row = c.fetchone()
    #print(row)

    # 读取表头字段值并写excel
    db_title = [i[0] for i in c.description]
    #print(db_title)
    ws.append(db_title)
    #把查询到的元组转换列表值
    for a in c:
        list_A_B = list(a)
        #print (list_A_B)
        ws.append(list_A_B)
    c.close()
    conn.close()
    wb.save(table_name)
#创建Excel
def create_wb(wb,filename):
    wb.save(filename=filename)
    print ("新建Excel:"+filename+"成功")

