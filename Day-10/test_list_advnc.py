import os

folders = input("provide a list of folder names with spaces in between: ").split()
#print(folders)               #it gives you the output as list

for folder in folders:
    try:
       files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name, looks like this folder doesn't exist:" + folder )
        break

    print(" ==== listing files for the folder - " + folder) #output will be in a order and clear
    #print(files)
    for file in files:  #print files in the desried order
        print(file)

#since this a sample program to list out folders, refer "03-list-files-in-folders.py" program which is actual python program and written using python functions 

