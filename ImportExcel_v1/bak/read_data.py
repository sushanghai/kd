# -*- coding: utf-8 -*-
import xlrd
import xdrlib,sys
import os

def excel_table_byname(file='市局科通处监控点状态详情1130.xls',colnameindex=0,by_name=u'市局科通处_'):
    data = xlrd.open_workbook(file)
    table  = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        'print(row)'
        if row:
            app ={}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    print(list)
    return list
excel_table_byname()
