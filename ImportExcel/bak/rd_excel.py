# -*- coding: utf8 -*-
#!/usr/bin/python
import xlrd
import read_config

def excel(fname):
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
         sh = bk.sheet_by_name("sheet1")
    except:
        print ("no sheet in %s named Sheet1" % fname)


if __name__ == '__main__':
    excel(read_config)

