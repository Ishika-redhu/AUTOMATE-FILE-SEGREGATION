import os
import shutil

from_dir="C:/Users/ishik/Downloads"              
to_dir="C:/Users/ishik/Documents/Document_Files" 
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.pdf','.doc','.txt','.docx']:
        path1=from_dir+'/'+file_name
        path2= to_dir
        path3= to_dir+'/' + file_name
        print(path1)
        print(path2)
        print(path3)
    if os.path.exists(path2):
        print("Moving"+file_name+"..........")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("Moving"+file_name+"..........")
        shutil.move(path1,path3)