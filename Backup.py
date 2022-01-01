import shutil
import os

source = input("Enter source folder name: ")
destination = input("Enter destination folder name: ")
source = source+'/'
destination = destination+'/'

listOfFile = os.listdir(source)

for i in listOfFile:
    shutil.copy((source+i), destination)
