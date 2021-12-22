from abc import ABC ,abstractmethod


class File(ABC):
    @abstractmethod
    def __init__(self,file_name,file_content,created_by,file_size):
        self.file_name = file_name
        self.file_content = file_content
        self.created_by = created_by
        self.file_size = file_size

class AsMail_Mixin(ABC):
    @abstractmethod
    def as_email_format(self):
        pass

    @abstractmethod
    def send(self,sender_mail, *email_addrs):
        pass

class PlayableFile_Mixin(ABC):
    @abstractmethod
    def __init__(self):
        self.volume = 0

    def volume_up(self):
        self.volume+=5

    def volume_down(self):
        self.volume-=5

    @abstractmethod
    def play(self):
        print(f"volume {self.volume}")

class MediaFile(File, PlayableFile_Mixin):
    @abstractmethod
    def __init__(self,file_name,file_content,created_by,file_size,duration):
        File.__init__(self,file_name,file_content,created_by,file_size)
        PlayableFile_Mixin.__init__(self)
        self.duration = duration

    @abstractmethod
    def play(self):
        PlayableFile_Mixin.play(self)
        for i in range(self.duration):
            print(i)


