# -*- coding: utf-8 -*-
import xlrd
import xdrlib,sys
import os

def open_excel(file='市局科通处监控点状态详情1130.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except:
        print("no sheet in %s named Sheet1" % file)
open_excel()
