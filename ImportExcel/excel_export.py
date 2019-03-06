# _*_ coding:utf-8 _*_
from openpyxl import Workbook
import cx_Oracle as oracle
import os
import xm_rdxlpath
'读取数据库信息'
dburl = xm_rdxlpath.RdPath().rdoracl()
#print(dburl)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn =oracle.connect(dburl)
cursor=conn.cursor()
'查询数据库语句'
table_sql = 'select * from result order by 设备编号'
#print (table_sql)
'表名'
month_str = xm_rdxlpath.RdPath().rdmonth()
month_list = xm_rdxlpath.RdPath().rdmonth().split(',')
table_name = month_list[0] + '月在线率.xlsx'
sheet_name = month_list[0] + '月在线率'
print (sheet_name)

def excel_export(wb):
    create_wb(wb,table_name)
    ws = wb.create_sheet(title=sheet_name, index=0)
    cursor.execute(table_sql)
    #row = cursor.fetchone()
    #print(row)

    # 读取表头字段值并写excel
    db_title = [i[0] for i in cursor.description]
    #print(db_title)
    ws.append(db_title)
    #把查询到的元组转换列表值
    for a in cursor:
        list_A_B = list(a)
        #print (list_A_B)
        ws.append(list_A_B)
    cursor.close()
    conn.close()
    wb.save(table_name)
#创建Excel
def create_wb(wb,filename):
    wb.save(filename=filename)
    #print ("新建Excel："+filename+"成功")
if __name__ == '__main__':
    wb = Workbook()
    excel_export(wb)