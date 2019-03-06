# _*_ coding:utf-8 _*_
import xlrd
import cx_Oracle as oracle
import os
import xm_rdxlpath
'数据库连接配置'
dburl = xm_rdxlpath.RdPath().rdoracl()
#print(dburl)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn =oracle.connect(dburl)
cursor=conn.cursor()
'读取配置文件的excel路径并转换'
file = xm_rdxlpath.RdPath().rdxl()[0]
#print(file)
xlfile_name = file.split(",")
#print(xlfile_name[0])
sheet = xm_rdxlpath.RdPath().rdxl()[1]
sheet_name = sheet.split(",")
#print(sheet_name[0])
'打开excel'
for excel_name in range(len(xlfile_name)):
    #print(excel_name)
    #print(xlfile_name[excel_name])
    data = xlrd.open_workbook(xlfile_name[excel_name])
    #print(data)
    '获取sheet名称'
    for excel_sheet_name in range(len(sheet_name)):
       # print(excel_sheet_name)
        #print (sheet_name[excel_sheet_name])
        table = data.sheet_by_name(sheet_name[excel_sheet_name])
        #print(table)
        '获取行数和列数'
        nrows = table.nrows
        ncols = table.ncols
        '循环行列表数据'
        for i in range(1,nrows):
            list = table.row_values(i)
            sql = "insert into MONTHTOTAL(SBBH,ZT,DATETIME) values ('" + str(list[0]) + "','" + str(list[10]) + "','" + str(
        list[13]) + "')"
            print(sql)
            cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()


