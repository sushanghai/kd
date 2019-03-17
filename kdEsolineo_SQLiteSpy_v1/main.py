# -*- coding: utf-8 -*-
import insertDB
import export_data
from openpyxl import Workbook
wb = Workbook()


def main():
    insertDB.insertDB()
    export_data.excel_export(wb)


if __name__ == "__main__":
    main()



