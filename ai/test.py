
# -*- coding:utf-8 -*-

import os, sys
import configparser
from os.path import join, getsize
print ('-')
#config = ConfigParser.RawConfigParser()
config = configparser.ConfigParser()
config.read('D:/dev/ConfigFile.properties')
print ('-')
#print config.get('File_info', 'file_info.base_path');

# Open a file
path_df = "D:/dev/"

paths =  os.path.dirname(path_df)

files =  os.path.basename(path_df)

abspath =  os.path.abspath(path_df)

listdir_path =  os.listdir(path_df)

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
    for (path, dir, files) in os.walk(base_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            print ("%s/%s" % (path, filename))
            #if ext == '.py':
            #print("%s/%s" % (path, filename))

#getFiles(config.get('File_info', 'file_info.base_path'))
fileSizeSum = 0;
for root, dirs, files in os.walk(config.get('File_info', 'base_path')):
#for root, dirs, files in os.walk('.'):

    result = "%s : %.f MB in %d files." % (os.path.abspath(root), sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0), len(files))
    print (result)
    fileSizeSum = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0) + fileSizeSum

    #print result

#print fileSizeSum
