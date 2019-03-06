#coding=utf-8
import os
import shutil
import datetime
import logging
import config_path
import time
from threading import Timer

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
'获取程序每隔多久运行的时间'
run_time = config_path.run_time()
# print(run_time)


def delete_file():
    '获取配置目标文件夹'
    dest_dir = config_path.dest_path()
    # print(dest_dir)
    '遍历文件夹下的所有文件'

    '获取配置文件中的数量'
    file_count = config_path.count()
    '获取当前时间'
    now = datetime.datetime.now()
    # print(now)
    '过期时间'
    old_time = config_path.old_time()
    # print(old_time)
    old_day = datetime.timedelta(seconds=int(old_time))
    # print(old_day)
    # print (now-old_day)
    a = 0
    file_list = os.listdir(dest_dir)
    print('文件总数'+str(len(file_list))+'个')
    logger.info('查询文件夹下文件总数' + str(len(file_list)) + '个')
    for i in range(0,len(file_list)):
        #print(i)
        if i < int(file_count):
            file_path = os.path.join(dest_dir,file_list[i])
            #print(file_path)
#            '文件创建时间'
#            file_ctime = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            '文件修改时间'
            file_chagetime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            #print(file_path,file_chagetime)
            #print(file_path,file_ctime)
            if file_chagetime < (now-old_day):
                if os.path.isdir(file_path):
                    try:
                        '递归删除文件及目录'
                        shutil.rmtree(file_path)
                        logger.info("删除文件夹%s,修改时间为%s" %(file_path,file_chagetime))
                        print("删除文件夹%s,修改时间为%s" %(file_path,file_chagetime))
                        a = a + 1
                    except Exception as e:
                        logger.info(e)
                        print(e)
                else:
                    continue
 #                   try:
 #                       '删除文件'
#                        os.remove(file_path)
#                        logger.info("删除文件%s" %file_path)
#                    except:
#                        logger.info("remove %s error." %file_path)
    logger.info('删除修改时间大于%s秒前的文件总数%s个.' % (old_time , a))
    print('删除修改时间大于%s秒前的文件总数%s个.' % (old_time , a))


def run():
    timer_interval = 1
    t = Timer(timer_interval,delete_file)
    t.start()
    while True:
        time.sleep(run_time)
        t = Timer(timer_interval , delete_file)
        t.start()
        print("程序运行中")


if __name__ == '__main__':
    run()
