from FileSystem_targil2.WordFile import WordFile
from FileSystem_targil2 import absract_classes

class PDFFile(WordFile):
    def __init__(self,file_name, file_content, created_by, file_size,is_writable):
        WordFile.__init__(self,file_name, file_content, created_by, file_size)
        self.is_writable = is_writable


    def cheak_pdf(self):
        if self.is_writable:
            self.change_pdf()
        else:
            print("can’t change file_content its pdf format ")

    def change_pdf(self):
        print("IN CHANGE PDF")



