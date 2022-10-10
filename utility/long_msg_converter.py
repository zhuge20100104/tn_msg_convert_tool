
class LongMsgConvertor(object):
    def __init__(self, file_path) :
        self.file_path = file_path
        
    def convert(self):
        content_ = ""
        contents = open(self.file_path).readlines()
        for line in contents:
            content_ += line.replace("\n", " ").replace('"', '\\"')
        return content_