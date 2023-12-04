import os 
import shutil 
from_dir="/Users/anikalal/Downloads/C102_assets-main"
to_dir="/Users/anikalal/Downloads/assets"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,exstention=os.path.splitext(file_name)
    print(name)
    print(exstention)
    if exstention=="":
        continue
    if exstention in [".gif",".png",".jpj",".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)

