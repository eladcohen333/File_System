from FileSystem_targil2.absract_classes import MediaFile
from FileSystem_targil2.absract_classes import PlayableFile_Mixin

class MovieFile(MediaFile):
    def __init__(self,file_name,file_content,created_by,file_size,duration,movie_name,director):
        super().__init__(file_name,file_content,created_by,file_size,duration)
        self.movie_name = movie_name
        self.director = director

    def play(self):
        print(f" movie name :  {self.movie_name}, director by: {self.director}")
        MediaFile.play(self)

