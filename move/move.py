#coding=utf-8
import os
import logging
import logging.config
import shutil
import config_path
import time
from threading import Timer
import datetime

'创建日志文件夹'
config_path.log_path()
'获取程序每隔多久运行的时间'
run1_time = int(config_path.run1_time())
# print(run1_time)

logging.config.fileConfig('config/log.ini')
logger = logging.getLogger('rotatingFileLogger')

def file_move():
    '获取配置文件的原文件夹'
    source_dir = config_path.source_path()
    # print(source_dir)

    '获取配置文件中的目标文件夹'
    dest1_dir = config_path.dest1_path()

    '获取配置文件中的数量'
    file_count = int(config_path.count1())
    # print(file_count)

    '获取当前时间'
    now = datetime.datetime.now()
    #print(now)

    '过期时间'
    old_time = config_path.old_time()
    # print(old_time)
    old_day = datetime.timedelta(seconds=int(old_time))
    #print(old_day)
    #print (now-old_day)

    '遍历原文件夹下的所有文件'
    file_list = os.listdir(source_dir)
    logger.info('文件总数' + str(len(file_list)) + '个')
    a = 0
    for i in range(0,len(file_list)):
        #print(i)
        if i < file_count:
            try:
                path = os.path.join(source_dir,file_list[i])
                #print(path)
                '查询文件创建时间'
                file_ctime = datetime.datetime.fromtimestamp(os.path.getctime(path))
                #print(path,file_ctime)
                '判断创建时间是否早于某个时间段'
                if file_ctime < (now - old_day):
                    #print(os.path.splitext(path)[-1])
                    '判断是否'
                    if os.path.splitext(path)[-1] == ".zip":
                        shutil.move(path,dest1_dir)
                        logger.info("移动文件从%s到%s，创建时间为%s"%(path,dest1_dir,file_ctime))
                        a = a+1
                    else:
                        print(path)
                        continue
                else:
                    continue
            except Exception as e:
                logger.error(e)
                print(e)
        else:
            continue
    logger.info('文件总数' + str(len(file_list)) + '个,'+"完成%s个文件移动" % a)
    #print('文件总数' + str(len(file_list)) + '个,'+"完成%s个文件移动" % a)

def run():
    timer_interval = 1
    t = Timer(timer_interval,file_move)
    t.start()
    while True:
        time.sleep(run1_time)
        t = Timer(timer_interval , file_move)
        t.start()
    #   print("程序运行中")


if __name__ == '__main__':
    run()
