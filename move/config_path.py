#coding:utf-8
import configparser
import os
import sys
sys.path.append(r'D:\\python\\move\\frozendir.py')
#print(sys.path)
import frozendir
APP_DIR =  frozendir.app_path()
#print(APP_DIR)

def source_path():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    source_path = conf.get('path', 'source_path')
    #print(source_path)
    return source_path


def dest1_path():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    dest1_path = conf.get('path', 'dest1_path')
    #print(dest1_path)
    return dest1_path
def dest2_path():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    dest2_path = conf.get('path', 'dest2_path')
    #print(dest2_path)
    return dest2_path

def count1():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    count1 = conf.get('count', 'count1')
    return count1

def count2():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    count2 = conf.get('count', 'count2')
    return count2

def run1_time():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    run1_time = conf.get('run_time', 'run1_time')
    #print(run1_time)
    return run1_time

def run2_time():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    run2_time = conf.get('run_time', 'run2_time')
    #print(run2_time)
    return run2_time

def old_time():
    config_path = os.path.join(APP_DIR, 'config')
    #print(config_path)
    if not os.path.exists(config_path):
        return None
    config_file = os.path.join(config_path, 'config.ini')
    #print(config_file)
    if not os.path.exists(config_file):
        return None
    conf = configparser.ConfigParser()
    conf.read(config_file, encoding='UTF-8')
    old_time = conf.get('old_time', 'old_time')
    #print(dest_path)
    return old_time

def log_path():
    config_path = os.path.join(APP_DIR, 'log')
    #print(config_path)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
        #print("创建日志文件夹成功")
    else:
        return None
