def call():
    print("*"*30)

class ContextManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file= None

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exctype,excinstance,traceback):
        self.file.close()

fname=input("Enter Filename: ")

def printCall():
    with ContextManager("readText.txt",'r') as f:
        line=f.readline()
        while line:
            call()
            print("{}".format(line.strip()))
            line=f.readline()
        call()


printCall()
    