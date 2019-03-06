import configparser
import os

cur_path=os.path.dirname(os.path.realpath(__file__))
'print (cur_path) 打印出目录路径'

config_path=os.path.join(cur_path,'config.ini')
'print (config_path)打印出文件路径'
conf = configparser.ConfigParser()
conf.read(config_path)

'获取db连接配置信息'
db_host = conf.get('oracle', 'db_host')
'print (db_host)'
db_user = conf.get('oracle', 'db_user')
db_pass = conf.get('oracle', 'db_pass')
db_port = conf.get('oracle', 'db_port')
'获取excel的配置文件'
book_name_xls = conf.get('excel','book_name_xls')
print (book_name_xls)
sheet_name_xls = conf.get('excel','sheet_name_xls')
print (sheet_name_xls)
