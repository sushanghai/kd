# _*_ coding:utf-8 _*_
import xlrd
import xlwt
import cx_Oracle as oracle
import os
import xm_rdxlpath
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

#以下为创建查询后的表
for i in range(len(day_list)):
    day = day_list[i]
    #print(day)
    rr = '\'%%%s-%s%%\'' % (month_list[0],day)
    table_A = 'A%s' % (day)
    table_D = 'D%s' % (day)
    #print(rr)
    #print(table_D)
    temp_sql = "create  table " + table_A + " as select b.sbbh,a.zt as "+ table_D + " from monthtotal a,source_data b where a.sbbh = b.sbbh and a.datetime like "+ rr + " order by sbbh"
    print(temp_sql)
    cursor.execute(temp_sql)
select_sql = "create table result as select a.sbbh as 设备编号,a.sbmc as 设备名称,a.yhz as 建设单位," + query[0] + " from SOURCE_DATA  a " + query[1]
print(select_sql)
cursor.execute(select_sql)
#以下为删除建立的临时表
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