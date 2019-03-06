#coding:utf-8
import os
import logging
import logging.config
import shutil
import config_path
import time
import datetime
import threading
import sys
#print(sys.getdefaultencoding())

'创建日志文件夹'
config_path.log_path()
'获取配置文件的原文件夹'
source_dir = config_path.source_path()
# print(source_dir)
'获取程序每隔多久运行的时间'
run1_time_1 = config_path.run1_time()
# print(run_time)
'获取程序每隔多久运行的时间'
run2_time_2 = config_path.run2_time()
# print(run_time)
'获取配置文件中的目标文件夹'
dest1_dir = config_path.dest1_path()
'获取配置文件中的目标文件夹2'
dest2_dir = config_path.dest2_path()
#print(dest2_dir)
'获取配置文件中的数量'
count1_1 = config_path.count1()
count2_2 = config_path.count2()
'过期时间'
old_time_1 = config_path.old_time()
# print(old_time)

if not os.path.exists(source_dir):
    print("请配置原文件夹路径配置source_path的路径,例如:D:\\test1")
elif not os.path.exists(dest1_dir):
    print("请配置目标文件夹dest1_path的路径,例如:D:\\test2")
    os._exit(0)
elif not os.path.exists(dest2_dir):
    print("请配置目标文件夹dest1_path的路径,例如:D:\\test4")
    os._exit(0)
elif not count1_1:
    print("请配置移动目标文件夹1的数量,例如:count1=1")
    os._exit(0)
elif not count2_2:
    print("请配置移动目标文件夹1的数量,例如:count2=2")
    os._exit(0)
elif not run1_time_1:
    print("请配置移动目标文件夹1的数量,例如:run1_time=1")
    os._exit(0)
elif not run2_time_2:
    print("请配置移动目标文件夹1的数量,例如:run2_time=2")
    os._exit(0)
elif not old_time_1:
    print("请配置移动目标文件夹1的数量,例如:old_time=2")
    os._exit(0)
else:
    count1 = int(count1_1)
    #print(count1)
    count2 = int(count2_2)
    #print(count2)
    run1_time = int(run1_time_1)
    #print(run1_time)
    run2_time = int(run2_time_2)
    #print(run2_time)
    old_time = int(old_time_1)
    #print(old_time)
logging.config.fileConfig("config/log.ini")
logger = logging.getLogger(name="rotatingFileLogger")

threadLock = threading.Lock()
def file_move(destpath,file_count):
    threadLock.acquire()
    '遍历原文件夹下的所有文件'
    file_list = os.listdir(source_dir)
    #print(file_list)
    #logger.info('文件总数' + str(len(file_list)) + '个')
    '获取当前时间'
    now = datetime.datetime.now()
    #print(now)
    old_day = datetime.timedelta(seconds=int(old_time))
    #print(old_day)
    #print (now-old_day)
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
                        #print(os.path.join((path,destpath)))
                        shutil.move(path,destpath)
                        logger.info("移动文件从%s到%s，创建时间为%s"%(path,destpath,file_ctime))
                        #print("移动文件从%s到%s，创建时间为%s" % (path, destpath, file_ctime))
                        a = a+1
                    else:
                        #print(path)
                        continue
                else:
                    continue
            except Exception as e:
                logger.error(e)
                print(e)
        else:
            continue
    file_list2 = os.listdir(source_dir)
    logger.info('文件总数' + str(len(file_list)) + '个,'+"完成%s个文件从%s到%s的移动," % (a,source_dir,destpath)+'剩余文件总数' +str(len(file_list2)) + '个。')
    threadLock.release()

def thread1():
    while True:
        time.sleep(run1_time)
        t1 = threading.Thread(target=file_move,name='move_1',args=(dest1_dir,count1))
        t1.start()
        t1.join()

def thread2():
    while True:
        time.sleep(run2_time)
        t2 = threading.Thread(target=file_move,name='move_2',args=(dest2_dir,count2))
        t2.start()
        t2.join()

def run():
    threads = [threading.Thread(target=thread1), threading.Thread(target=thread2)]
    for t in threads:
        t.start()

if __name__ == '__main__':
    run()
