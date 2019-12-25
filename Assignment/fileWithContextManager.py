class contextManager:
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

with contextManager(fname,'r') as f:
    print(f.read())


print("File Closed")
