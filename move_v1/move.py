#coding=utf-8
import os
import logging
import shutil
import config_path
import time
from threading import Timer
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def file_move():
    '获取配置文件的原文件夹'
    source_dir = config_path.source_path()
    # print(source_dir)

    '获取配置文件中的目标文件夹'
    dest_dir = config_path.dest_path()
    dest2_dir = config_path.dest2_path()
    '获取配置文件中的数量'
    file_count = config_path.count()
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
    print('文件总数' + str(len(file_list)) + '个')
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
                        if os.path.exists(path):
                            shutil.move(path,dest_dir)
                            logger.info("移动文件从%s到%s，创建时间为%s"%(path,dest_dir,file_ctime))
                            a = a+1
                        else:
                            continue
                    else:
                        print(path)
                        shutil.move(path,dest2_dir)
                        continue
                else:
                    continue
            except Exception as e:
                logger.error(e)
                print(e)
        else:
            continue
    logger.info("完成%s个文件移动" % a)
    print("完成%s个文件移动" % a)

def run():
    '获取程序每隔多久运行的时间'
    run_time = config_path.run_time()
    # print(run_time)
    timer_interval = 1
    t = Timer(timer_interval,file_move)
    t.start()
    while True:
        time.sleep(run_time)
        t = Timer(timer_interval , file_move)
        t.start()
    #   print("程序运行中")


if __name__ == '__main__':
    run()
