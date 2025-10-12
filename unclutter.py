import os
import shutil
# Functions
def file_extrector():
    items = os.listdir(folder)
    for item in items:
     source_link = os.path.join(folder,item)
     if os.path.isfile(source_link): # validating file not sub-folder
       name , ext = os.path.splitext(item)
     # if(ext  
       if ext.lower() in [".jpg",".jpeg",".png"]:
           new_sub_folder = os.path.join(folder,"photos")
       else:
          new_sub_folder = os.path.join(folder,ext[1:].upper())
       os.makedirs(new_sub_folder, exist_ok=True)
     # Making destination link to move
       destination_link = os.path.join(new_sub_folder,item)
       shutil.move(source_link,destination_link)
       print(f"Moved {item} to folder {new_sub_folder}")


# main code
folder = input("Enter the full folder path: ")
if os.path.exists(folder):
    print("folder exist")
    file_extrector()
    
else:
   print('folder not found')