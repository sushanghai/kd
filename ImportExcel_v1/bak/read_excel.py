import xlrd
import cx_Oracle as oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn = oracl.connect('ezview/ezview@35.48.90.88:1521/orcl')
cursor = conn.cursor()


data = xlrd.open_workbook('市局科通处监控点状态详情1130.xls')
'通过索引顺序获取'
'''table = data.sheet()[0]
'通过索引顺序获取'
table = data.sheet_by_index(0)
'通过名称获取'''
table = data.sheet_by_name(u'市局科通处_')

'获取整行和整列的值(数组)'
'table.row_values(i)'

'table.col_values(i)'

'获取行数和列数'
nrows = table.nrows

ncols = table.ncols


'循环行列表数据'
for i in range(1,nrows):
    'print (table.row_values(i))'
    list = table.row_values(i)
    'print(list[0],list[10],list[13])'
    sql =""


