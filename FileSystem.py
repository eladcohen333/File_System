import json
from copy import copy

from FileSystem_targil2.PDFFile import PDFFile
from FileSystem_targil2.PictureFile import PictureFile
from FileSystem_targil2.WordFile import WordFile
from FileSystem_targil2.MovieFile import MovieFile
from FileSystem_targil2.SongFile import SongFile

class FileSystem:

    def __init__(self):
        self.system = {} # save the files in dict

    def addFile(self, file_json):
        for item in file_json:
            cheak_file =item["file_name"].split(".")[-1]
            name_file = item["file_name"]
            size_file = item["file_size"]
            det_file = list(item.values())
            kind_of_file = self._cheak_kind(cheak_file, det_file, size_file) # sent to another fun for prpoer
            try:
                if kind_of_file == "pdf" and name_file  not in self.system.keys():
                      pd_file = PDFFile(det_file[0],det_file[1],det_file[2],det_file[3],det_file[4])
                      self.system[item["file_name"]] = (pd_file)
                elif kind_of_file == "word" and name_file  not in self.system.keys():
                      w_file = WordFile(det_file[0],det_file[1],det_file[2],det_file[3])
                      self.system[item["file_name"]] = (w_file)
                elif kind_of_file == "pic" and name_file  not in self.system.keys():
                      pic_file =  PictureFile(det_file[0],det_file[1],det_file[2],det_file[3],det_file[4],det_file[5])
                      self.system[item["file_name"]] = (pic_file)
                elif kind_of_file == "song" and name_file  not in self.system.keys() :
                      son_file = SongFile(det_file[0],det_file[1],det_file[2],det_file[3],det_file[4],det_file[5],det_file[6])
                      self.system[item["file_name"]] = (son_file)
                elif kind_of_file == "mov" and name_file  not in self.system.keys() :
                      miv_file = MovieFile(det_file[0],det_file[1],det_file[2],det_file[3],det_file[4],det_file[5],det_file[6])
                      self.system[item["file_name"]] = (miv_file)
            except: #if the file not proper
                  pass

    def _cheak_kind(self, cheak_file, det_file, size_file): # cheak the if the file proper according size and type
        max_size = 40
        if cheak_file == 'pdf' and  size_file<max_size:
            result = self._cheak_pdf(det_file) # send to another fun for cheak that the file dont have missing data
        elif cheak_file in ["doc", "docx"] and size_file<max_size:
            result = self._cheak_word(det_file)
        elif cheak_file in ["png", "jpeg", "jpg"] and  size_file<max_size:
            result = self._cheak_pic(det_file)
        elif cheak_file in ["mp3", "wav"] and  size_file<max_size:
            result = self._cheak_song(det_file)
        elif cheak_file in ["mp4", "avi"] and  size_file<max_size:
            result = self._cheak_mov(det_file)
        else:
            result = "this file not proper"
        return result

    # all this functions cheak that evry file dont have a missing data
    def _cheak_pdf(self, cheak_file):
       if len(cheak_file) == 5:
           return "pdf"
       else:
           return "no proper" #

    def _cheak_word(self, cheak_file):
        if len(cheak_file) == 4:
            return "word"
        else:
            return "no proper"

    def _cheak_pic(self, cheak_file):
        if len(cheak_file) == 6:
            return "pic"
        else:
            return "no proper"

    def _cheak_song(self, cheak_file):
        if len(cheak_file) == 7:
            return "song"
        else:
            return "no proper"

    def _cheak_mov(self, cheak_file):
        if len(cheak_file) == 7:
            return "mov"
        else:
            return "no proper"

    def deleteFile(self, file_name):
        if file_name in self.system.keys():
            del self.system[file_name]


    def getFiles(self, type_file):
        list_type = []
        for name,i in zip(self.system.values(), self.system):
            type_of_object = type(name)
            class_name = type_of_object.__name__
            if class_name == type_file:
                list_type.append(self.system[i])
        result = list_type if  len(list_type)  else self.system
        return  f"the files of type  are {result} "

# **********************************

    def cloneFile(self,file_name):
        for name, i in zip(self.system.keys(), self.system):
            if name == file_name:
                copy_file = copy(self.system[i])
                copy_file.file_name = "CLONE"+"_"+file_name
                self.system["CLONE"+"_"+file_name] = (copy_file)
                return copy_file.file_name, len(self.system)
        return "no found file like this name "

    def __str__(self): # function to cheak the len and files in the system
        return f"The size of the system its: {len(self.system)} \n now the system contain files :{self.system}"

    def concatFiles(self, file_name1, file_name2):
        if (file_name1.split(".")[-1] == file_name2.split(".")[-1]) and (file_name1, file_name2 in self.system):
            concat_file1 = vars(self.system[file_name1])
            concat_file2 = vars(self.system[file_name2])
            o_file = self._add_att(concat_file1, concat_file2) # sent to _add_att fun
            j_file = [o_file] # convert to json format
            new_onion_file = self.addFile(j_file) # add to the system (via addfile function)
        else:
            return (f"the files not same type or exist in the system")

    # this fun for connect betwin the attributes of the files
    def _add_att(self, concat_file1, concat_file2):
        union_file = {}
        list_val = []
        list_keys = list(concat_file1.keys())
        for v1, v2 in zip(concat_file1.values(), concat_file2.values()):
            if v1 and v2 is str:
                list_val.append(v1 + "-" + v2)
            else:
                list_val.append(v1 + v2)
        for at1, at2 in zip(list_keys, list_val):
            union_file[at1] = at2
        return union_file
