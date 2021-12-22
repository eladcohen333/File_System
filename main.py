import json
from FileSystem_targil2.FileSystem import FileSystem

if __name__ == '__main__':
    with open(r"C:\Users\DELL\Desktop\OOP\s_targil2_file.txt", "r") as file:# upload the file
        file_json = json.load(file)# convert to  json file
    files = FileSystem() # create object of Filesystem
    files.addFile(file_json) # add the file to system
    print(files) # cheak the size in sysdem(hoe many files) and return the files(objects)
    files.deleteFile("video1.mp4") # delete thid file from the system
    print(files) # option cheak the system again
    print(files.getFiles("PDFFile")) # cheak the type of files
    files.cloneFile("pic2.jpeg") # add clone file (if exsist)
    # print(files)
    files.concatFiles("pic3.jpeg","pic2.jpeg") # create object from 2 same type(if exists)
    # print(files)
