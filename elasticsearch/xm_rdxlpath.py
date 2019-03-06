# -*- coding:utf-8 -*-
import configparser
import os
class RdPath:
    def rdoracl(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        db_url = conf.get('oracle','db_url')
        return db_url

    def rdes(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        es_url = conf.get('es', 'es_url')
        return es_url

    def rdtime(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        es_time = conf.get('es_time', 'es_time')
        #print(es_time)
        return es_time

    def rddate(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        config_file = os.path.abspath(os.path.join('config', 'config.ini'))
        conf = configparser.ConfigParser()
        conf.read(config_file, encoding='UTF-8')
        es_date = conf.get('es_date', 'es_date')
        #print(es_date)
        return es_date

if __name__ == '__main__':
    RdPath().rdoracl()
    RdPath().rdes()
    print(RdPath().rdtime())
    print(RdPath().rddate())