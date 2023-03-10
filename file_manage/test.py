# -*- coding:utf-8 -*-
import logging
import os, sys
import ConfigParser
from os.path import join, getsize
from datetime import datetime
import os.path, time
import platform
import json

config = ConfigParser.RawConfigParser()

if platform.system() ==  'Windows':
    config.read('D:/TEST/ConfigFile.properties')
else :
    config.read('/app/ConfigFile.properties')


logging.basicConfig(filename="deleteFileList.log", format='%(asctime)s %(message)s', filemode='w') 
#logging.basicConfig(filename="deleteFileList.log", level=logging.INFO)

 #Creating an object 
logger=logging.getLogger() 

#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.INFO) 
#logger.setLevel(logging.DEBUG) 

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
#logger.warning('Protocol problem: %s', 'connection reset', extra=d)
## properties File
#print config.get('File_info', 'file_info.base_path');


def search(dirname):
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                #if ext == '.py': 
                #    print(full_filename)
        pass


def getFiles(base_path):
    #print platform.system()
    file_list = []

    for (path, dir, files) in os.walk(base_path):
        #print path
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            #fileFullPath = "%s/%s" % (path, filename)
            if platform.system() ==  'Windows':
                fileFullPath = path + config.get('Default_option', 'windows_path')  + filename
            else :
                fileFullPath = path + config.get('Default_option', 'linux_path')  + filename
                #print fileFullPath
            file_list.append(fileFullPath)
            # for target_folder in json.loads(config.get('File_info', 'base_path_folders')):       
            #     #file_list = getFiles(config.get('File_info', 'base_path')+'/'+str(target_folder))
            #     #if os.path.isfile(base_path+'/'+str(target_folder)) ===  True  and os.path.isfile(base_path+'/'+str(target_folder)) ===
            #     if  base_path+'/'+str(target_folder) != fileFullPath:
            #         print '- ' + fileFullPath
            #         file_list.append(fileFullPath)
                #print '###' + fileFullPath
            #diffDayTime(fileFullPath)
    return file_list          


# def diffDayTime(targetFiles):
#     file_list = []
#     for file in targetFiles:
#         #??????????????????
#         mtime = os.path.getmtime(file)
#         mtime_format = datetime.datetime.fromtimestamp(mtime)

#         #????????????
#         ctime = os.path.getctime(file)
#         ctime_format = datetime.datetime.fromtimestamp(ctime)

#         #????????????(?????????)
#         diff_m_Time = datetime.datetime.now() - mtime_format
#         diff_m_Time_list = str(diff_m_Time).split(' ')

#         diff_c_Time = datetime.datetime.now() - ctime_format
#         diff_c_Time_list = str(diff_c_Time).split(' ')

#         # ?????? ????????? ????????? ?????????
#         if len(diff_m_Time_list) > 2 :
#             if int(diff_m_Time_list[0]) > int(config.get('OPTION', 'day')) :  
#                  file_list.append(file);
#                  logger.info("##" +  file)
#                  logger.info( " - diffDateTime: %s" % diff_m_Time_list)
#                  logger.info( " - last modified: %s" % time.ctime(os.path.getmtime(file)))
#                  logger.info( " - created: %s" % time.ctime(os.path.getctime(file)))     
#     logger.info( "=============================== total : %s" % len(file_list))        
  
#     return  file_list


    

def diffDayTime(targetFile):

    is_chk = False

    #??????????????????
    mtime = os.path.getmtime(targetFile)
    mtime_format = datetime.fromtimestamp(mtime)

    #????????????
    ctime = os.path.getctime(targetFile)
    ctime_format = datetime.fromtimestamp(ctime)

    #????????????(?????????)
    diff_m_Time = datetime.now() - mtime_format
    diff_m_Time_list = str(diff_m_Time).split(' ')

    diff_c_Time = datetime.now() - ctime_format
    diff_c_Time_list = str(diff_c_Time).split(' ')

    # ?????? ????????? ????????? ?????????
    if len(diff_m_Time_list) > 2 :
        if int(diff_m_Time_list[0]) > int(config.get('OPTION', 'day')) :  
                logger.info("##" +  targetFile)
                logger.info( " - diffDateTime: %s" % diff_m_Time_list)
                logger.info( " - last modified: %s" % time.ctime(os.path.getmtime(targetFile)))
                logger.info( " - created: %s" % time.ctime(os.path.getctime(targetFile)))
                is_chk = True
    return is_chk  
   


# def getPathSize(targetPath):

#     # getFiles(config.get('File_info', 'file_info.base_path'))
#     fileSizeSum = 0;
#     for root, dirs, files in os.walk(targetPath):
#     #for root, dirs, files in os.walk('.'):
#         result = "%s : %.f MB in %d files." % (os.path.abspath(root), sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0), len(files))
#         fileSizeSum = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0) + fileSizeSum

#     return fileSizeSum

import enum
# Enum for size units
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

# def getPathSize(size_in_bytes, unit):
#    if unit == SIZE_UNIT.KB:
#        return size_in_bytes/1024
#    elif unit == SIZE_UNIT.MB:
#        return size_in_bytes/(1024*1024)
#    elif unit == SIZE_UNIT.GB:
#        return size_in_bytes/(1024*1024*1024)
#    else:
#        return size_in_bytes


# size_in_bytes ??? float ????????????
def getPathSize(size_in_bytes, unit):

   if unit == 'a':
       return size_in_bytes/1024
   elif unit == 'b':
       return size_in_bytes/(1024*1024)
   elif unit =='c' :
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes
     


def deleteFile(targetFiles):
    if(config.get('OPTION', 'delete_yn') == 'Y') : 
        print 'Delete'    



def fillter_folder(folder_name):
    is_chk = False
    for target_folder in json.loads(config.get('File_info', 'base_path_folders')):
        if str(folder_name).strip() == str(target_folder).strip():          
            is_chk =  True
            break;
    return is_chk


def load_to_target_folder(base_path):
    target_path = [];
    for (path, dir, files) in os.walk(config.get('File_info', 'base_path')):      
        if path == config.get('File_info', 'base_path'): 
            #????????????
            for target_folder in dir:
                if fillter_folder(target_folder) == False:
                    fileFullPath = path + target_folder
                    target_path.append(fileFullPath)

    return target_path

    
def write_history_file(file_list , target_folder):

    if len(file_list[0]) > 0:
        today = datetime.today().strftime('%Y-%m-%d')
        if platform.system() ==  'Windows':
            if target_folder != '':
                path = os.getcwd()+'\\'+target_folder+'_'+today
                print path
            else:
                path = os.getcwd()+'\\'+'log_'+today
        else :
            if target_folder != '':
                path = os.getcwd()+config.get('Default_option', 'linux_path')+target_folder+'_'+today
            else:
                path = os.getcwd()+config.get('Default_option', 'linux_path')+'log_'+today
        f = open(path, 'a')

        total_file_size = 0
        for file in file_list[0] :
            if os.path.isfile(file):

                ############### ????????? ?????? ?????? ?????????  #################+
                #?????????
                size = getPathSize(float(os.path.getsize(file)),'b')
                total_file_size = total_file_size + size

                #?????????
                last_modified = time.ctime(os.path.getmtime(file))
                last_modified_format = datetime.strptime(last_modified, "%a %b %d %H:%M:%S %Y")

                #?????????
                created =  time.ctime(os.path.getctime(file))
                created_format = datetime.strptime(created, "%a %b %d %H:%M:%S %Y")  
                f.write(file +'\n' + ' - ???????????? : ' +str(size)+ ' MB'+ '\n' + ' - ????????? : ' +str(created_format)+'\n' + ' - ????????? : ' +str(last_modified_format)+ '\n')
        f.write(' #################### ??? ?????? ?????? : '  +str(total_file_size)+ ' MB'+ '\n')      
        f.write(' #################### ??? ?????? ??? : ' + str(len(file_list[0]))+ '???'+ '\n')      
        f.close()


def write_common_history(coment,file_name):
     today = datetime.today().strftime('%Y-%m-%d')
     if platform.system() ==  'Windows':
            if file_name != '':
                path = os.getcwd()+config.get('Default_option', 'windows_path')+file_name
            else:
                path = os.getcwd()+config.get('Default_option', 'windows_path')+today
     else :
            if file_name != '':
                path = os.getcwd()+config.get('Default_option', 'linux_path')+file_name
            else:
                path = os.getcwd()+config.get('Default_option', 'linux_path')+today

     f = open(path, 'a')
     f.write(coment)
     f.close()


def do_filter(file_list , target_folder):

    # ?????? ?????????
    info = []

    # ???????????? ?????? ?????????
    load_target_file = []

    # ?????? ?????????
    sub_total_size = 0;

    
    for file in file_list:
        ## ?????? ?????? ??? ????????? ??????
        if diffDayTime(file) == True :
            load_target_file.append(file)
            #write_history_file(file , target_folder)
            sub_total_size = sub_total_size + os.path.getsize(file)
    info.append(load_target_file)
    info.append(str(getPathSize(float(sub_total_size),'b')))
    #write_common_history('==============sub total' + str(getPathSize(float(sub_total_size),'b'))+'\n')
    #print info
    
    return info
      

def doTask():
    
    ### ??????

    # 1. pid?????? (pid ??????????????? ????????????)
    # - ????????????

    # 2. ???????????? ?????? ?????????
    target_folder_list = load_to_target_folder(config.get('File_info', 'base_path'))
    
    # 3. ???????????? ????????? ?????? ?????????
    for target_folder in target_folder_list :

        # 3-0
        total_file_size = 0;
        total_file_length = 0;

        # 3-1 ?????? ???????????? (???????????? ?????? ?????????)
        folder_name = ''
        if platform.system() ==  'Windows':
            folder_name =  target_folder.split('\\')[-1]
        else :
            folder_name =  target_folder.split('/')[-1]
            
         
        # 4. ???????????? ????????? ?????? ???????????? ??????
        full_path_target_file_list = getFiles(target_folder)
        
        # 5. ????????? ?????? ????????? Task (????????? ?????? ??????)
        log_file_info = do_filter(full_path_target_file_list , target_folder)

        # 6. ???????????? ?????? ?????? 
        write_history_file(log_file_info , folder_name)

    ### ???????????? ??????




        
        # ????????? ??????(????????????) ????????? (?????? ???????????? , ???????????? ??????.. ??????)    

    ## ??????

    #total = 0
    #filter_file_list = []

    #for target_folder in json.loads(config.get('File_info', 'base_path_folders')):       
        ##filter_file_list = getFiles(config.get('File_info', 'base_path')+'/'+str(target_folder))
    #    filter_file_list.append(config.get('File_info', 'base_path')+'/'+str(target_folder))
    #    target_File_path.append(config.get('File_info', 'base_path')+'/'+str(target_folder))
    #print os.path.abspath(config.get('File_info', 'base_path'))

                    #print target_folder
                    #print '--------------'

                #?????? ??????
                #for row in json.loads(config.get('File_info', 'base_path_folders')):
                    
                    #if str(row).strip() != str(target_folder).strip():
                    #    target_path_tmp.append(target_folder)
                    #    print '====>' + str(row).strip()


                    #if str(row).strip() != str(target_folder).strip():
                        #print '-' + str(target_folder).strip()
                        #print '-' + str(row).strip()

                        #print '->'+str(row).strip()
                        #if str(row).strip() != str(target_folder).strip():
                        #    print '*' + str(target_folder).strip()
                            #fileFullPath = path + target_folder
                            #target_path.append(fileFullPath)

                        #print str(row).strip()
                    #    print ''
        
                        #fileFullPath = path + folder
                        #target_path.append(fileFullPath)
    #print  target_path_tmp                  
    #print target_path
    #print set(target_path)
    #print target_path
            #for target_folder in json.loads(config.get('File_info', 'base_path_folders')):           
            #    if
    #print os.listdir(config.get('File_info', 'base_path'))
    #file_list = getFiles(config.get('File_info', 'base_path'))
    #do_filter(file_list)


     #   file_diff_list = diffDayTime(file_list)
     #   total = total + int(len(file_diff_list))
    #print '======Total : ' +   int(total)  

    #file_list = getFiles(config.get('File_info', 'base_path'))
    
    # ?????? ?????? (???????????? ?????? ???????????? ??????)
    #diffDayTime(file_list)

    # ????????????
    #deleteFIle(file_list)   

    #result = os.popen('dir/w').read()
    

## main run 
if __name__ == '__main__':
    #env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    # if env == 'dev':
    #     app.config = config.DevelopmentConfig
    # elif env == 'test':
    #     app.config = config.TestConfig
    # elif env == 'prod':
    #     app.config = config.ProductionConfig
    # else:
    #     raise ValueError('Invalid environment name')
    
   doTask();


####### ??????
# ???????????? 90??? ????????? ?????? ????????? ????????? ??????
#find /app/log/jeus/*.* -mtime +90 -exec rm -f {} \;
## ??????????????? ????????? ?????? ?????? ?????? ????????? copy
#find /app/log/jeus/*.* -mtime 90 -exec cp -ar {} /home/backup \;