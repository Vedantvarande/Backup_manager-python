import shutil
import os

path = input("Enter the name of the folder we need to sort:")

listOfFile = os.listdir(path)
for i in listOfFile:
    name, ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+i, path+'/'+ext+'/'+i)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+i, path+'/'+ext+'/'+i)
