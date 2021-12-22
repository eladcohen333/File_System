from FileSystem_targil2.absract_classes import MediaFile

class SongFile(MediaFile):
    def __init__(self,file_name,file_content,created_by,file_size,duration,song_name,artist):
        MediaFile.__init__(self,file_name,file_content,created_by,file_size,duration)
        self.artist = artist
        self.song_name = song_name

    def play(self):
        print(f"song name: {self.song_name}, artist name: {self.artist}")
        MediaFile.play(self)

