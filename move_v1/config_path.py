#coding=utf-8
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


def dest_path():
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
    dest_path = conf.get('path', 'dest_path')
    #print(dest_path)
    return dest_path
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

def count():
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
    count = conf.getint('count', 'count')
    #print(count)
    return count

def run_time():
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
    run_time = conf.getint('run_time', 'run_time')
    #print(run_time)
    return run_time

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