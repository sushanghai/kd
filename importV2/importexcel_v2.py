# _*_ coding:utf-8 _*_
import xlrd
import xm_rdxlpath
import os
import sqlite3
db_filename = 'database.db'
#db_is_new = not os.path.exists(db_filename)
def sqlite3_db_create():
    if not os.path.exists(db_filename):
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
        c.execute('''CREATE TABLE monthtotal(sbbh varchar(200),datetime varchar(200),zt varchar(200));''')
        conn.commit()
        conn.close()
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
'读取配置文件的excel路径并转换'
file = xm_rdxlpath.RdPath().rdxl()[0]
#print(file)
xlfile_name = file.split(",")
#print(xlfile_name[0])
sheet = xm_rdxlpath.RdPath().rdxl()[1]
sheet_name = sheet.split(",")
#print(sheet_name[0])
'打开excel'
def del_table():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    del_sql = "delete from monthtotal"
    cursor.execute(del_sql)
    conn.commit()
    cursor.close()
    conn.close()
def excel_import():
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    for excel_name in range(len(xlfile_name)):
        #print(excel_name)
        #print(xlfile_name[excel_name])
        data = xlrd.open_workbook(xlfile_name[excel_name])
        print(data)
        '获取sheet名称'
        for excel_sheet_name in range(len(sheet_name)):
            print(excel_sheet_name)
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

if __name__ == '__main__':
    sqlite3_db_create()
    del_table()
    excel_import()
