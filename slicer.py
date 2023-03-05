import os
import pandas as pd


print("CSV Slicer")
workDIr = os.path.abspath('.')
lst_files = []
for dirpath, dirnames, filenames in os.walk(workDIr):
    for filename in filenames:
        if filename[-3:] == 'csv':
            #print (filename)
            lst_files.append(filename)

print(f"target file(s) : {lst_files}\n\n")            
slice_size = 1000000


def save_csv(filename,df,max_file_count):
    for i in range(max_file_count):
        start_line = 0+i*slice_size
        end_line = slice_size+i*slice_size
        file_num = '{0:05d}'.format(i+1)
        save_name = filename + "_" + file_num + ".csv"
        print(f"file_name : {save_name}")
        if(i<max_file_count-1) :
            print(f"start : {start_line} \t end : {end_line}")
            print(f"file length : {len(df[start_line:end_line])}")
            df[start_line:end_line].to_csv(save_name,mode='w')
        else :
            print(f"start : {start_line} \t end : {start_line+len(df[start_line:])}")
            print(f"file length : {len(df[start_line:])}")
            df[start_line:].to_csv(save_name,mode='w')
            

for i in range(len(lst_files)):
    df = pd.read_csv(lst_files[i])    
    filename = lst_files[i]
    print("")
    print("")
    print(f"start : {filename}!")
    print("")
    if len(df)%slice_size == 0:
        max_file_count = len(df)//slice_size
    else :
        max_file_count = len(df)//slice_size + 1
    save_csv(filename,df,max_file_count)
    print("")
    print(f"finished : {filename}!")
    