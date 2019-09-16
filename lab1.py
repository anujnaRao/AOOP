import time

def timeCall(func):
	print("Time started")
	st=time.time()
	func()
	et=time.time()
	print("Time ended")
	diff=et-st
	print("Time taken: ",diff)
	return func

class Fibo:
	def __init__(self):
		self.a=0
		self.b=1

	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		return self.a
	def __iter__(self):
		return self

@timeCall
def call():
	fib=Fibo()
	n=int(input("Enter the n value: "))
	for f in range(n-1):
		print(next(fib))
	print(next(fib))
