import xlrd
import cx_Oracle as oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

conn =oracle.connect('ezview/ezview@192.168.31.31:1521/orcl')
cursor=conn.cursor()
'打开excel'
data = xlrd.open_workbook('test1.xls')
'通过名称获取'''
table = data.sheet_by_name(u'市局科通处_')

'获取行数和列数'
nrows = table.nrows
ncols = table.ncols

'循环行列表数据'
for i in range(1,nrows):
    list = table.row_values(i)
    sql = "insert into JMFJ(SBBH,ZT,DATETIME) values ('" + str(list[0]) + "','" + str(list[10]) + "','" + str(
        list[13]) + "')"
    print(sql)
    cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
