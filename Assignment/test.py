
class fileName:

    def deco_one(self,func):
        def inner():
            print("*"*40)
            func()
            print("*"*40)
        return inner

    @deco_one
    def printCall(self):
        print("Hello")

f= fileName()
f.printCall()
    