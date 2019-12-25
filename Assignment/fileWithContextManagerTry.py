
class contextManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file= 0

    def __entry__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exctype,excinstance,traceback):
        self.file.close()

f = open('hello.txt', 'w')
try:
    print(f.read())
finally:
    f.close()