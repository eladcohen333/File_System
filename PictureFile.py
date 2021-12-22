from FileSystem_targil2.absract_classes import File

class PictureFile(File):
    def __init__(self,file_name,file_content,created_by,file_size,dim_width,dim_height):
        super().__init__(file_name,file_content,created_by,file_size)
        self.dim_width = dim_width
        self.dim_height = dim_height


    def show_picture(self):
        size_pic = (self.dim_height)*(self.dim_width)
        print(f" hight is:{self.dim_height} , width is: {self.dim_width} , size of picture :{size_pic}")


