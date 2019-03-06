# _*_ coding:utf-8 _*_
import configparser
import os
class RdPath:
    def rdxl(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        #config_file = os.path.join(cur_path,'config.ini')
        #print(config_file)
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        #print(config_file)
        conf = configparser.ConfigParser()
        conf.read(config_file,encoding='UTF-8')

        excel_file = conf.get('excel','excel_file')
        #print(excel_file)
        sheet_name = conf.get('excel','sheet_name')
        #print(sheet_name)
        return excel_file,sheet_name

    def rdoracl(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        db_url = conf.get('oracle','db_url')
        return db_url

    def rdmonth(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        month = conf.get('rq', 'MONTH')
        return month


    def rdday(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        day = conf.get('rq', 'DAY')
        return day

    def select_AB(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        select_A = conf.get('query', 'SELECT_A')
        select_B = conf.get('query', 'SELECT_B')

        return select_A,select_B

if __name__ == '__main__':
    RdPath().rdxl()
    RdPath().rdoracl()
    RdPath().rdmonth()
    RdPath().rdday()
    RdPath().select_AB()