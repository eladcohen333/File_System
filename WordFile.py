from FileSystem_targil2.absract_classes import AsMail_Mixin,File

class WordFile(File, AsMail_Mixin):
    def __init__(self,file_name, file_content, created_by, file_size):
        File.__init__(self,file_name, file_content, created_by, file_size)

    def as_email_format(self):
         return f"{self.file_name} content: {self.file_content} of {self.created_by}   his size: {self.file_size}"

    def send(self,sender_mail, *email_addrs):
        email = self.as_email_format()
        return f"send {email} from {sender_mail} to {email_addrs}"
