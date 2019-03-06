# _*_ coding:utf-8 _*_
import cx_Oracle as oracle
import os
import xm_rdxlpath
from openpyxl import Workbook

'读取数据库信息'
dburl = xm_rdxlpath.RdPath().rdoracl()
#print(dburl)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn =oracle.connect(dburl)
cursor=conn.cursor()
'读取月信息'
month_str = xm_rdxlpath.RdPath().rdmonth()
month_list = xm_rdxlpath.RdPath().rdmonth().split(',')
#print(month_list[0])
day_str = xm_rdxlpath.RdPath().rdday()
day_list = xm_rdxlpath.RdPath().rdday().split(',')
#print(day_list[0])
'获取查询条件配置'
query = xm_rdxlpath.RdPath().select_AB()
#print(query_A[0])
#print(query_A[1])
'查询数据库语句'
table_sql = 'select * from result order by 设备编号'
#print (table_sql)
'表名'
table_name = month_list[0] + '月在线率.xlsx'
sheet_name = month_list[0] + '月在线率'
#print (sheet_name)

#以下为创建查询后的表
def create_temp():
    conn = oracle.connect(dburl)
    cursor = conn.cursor()
    for i in range(len(day_list)):
        day = day_list[i]
        #print(day)
        rr = '\'%%%s-%s%%\'' % (month_list[0],day)
        table_A = 'A%s' % (day)
        table_D = 'D%s' % (day)
        #print(rr)
        #print(table_D)
        temp_sql = "create  table " + table_A + " as select b.sbbh,a.zt as "+ table_D + " from monthtotal a,source_data b where a.sbbh = b.sbbh and a.datetime like "+ rr + " order by sbbh"
        #print(temp_sql)
        cursor.execute(temp_sql)
    select_sql = "create table result as select a.sbbh as 设备编号,a.sbmc as 设备名称,a.yhz as 建设单位," + query[0] + " from SOURCE_DATA  a " + query[1]
    #print(select_sql)
    cursor.execute(select_sql)
    conn.commit()
    cursor.close()
    conn.close()
#以下为删除建立的临时表
def delete_temp():
    conn = oracle.connect(dburl)
    cursor = conn.cursor()
    for j in range(len(day_list)):
        day = day_list[j]
        #print(day)
        table_A = 'A%s' % (day)
        drop_sql = "drop table " + table_A
        #print(drop_sql)
        cursor.execute(drop_sql)
    conn.commit()
    cursor.close()
    conn.close()
def drop_result():
    conn = oracle.connect(dburl)
    cursor = conn.cursor()
    drop_sql = 'drop table result'
    cursor.execute(drop_sql)
    conn.commit()
    cursor.close()
    conn.close()

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
    print ("新建Excel:"+filename+"成功")

if __name__ == '__main__':
    create_temp()
    delete_temp()
    wb = Workbook()
    excel_export(wb)
    drop_result()


