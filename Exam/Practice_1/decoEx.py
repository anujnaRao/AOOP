import time


def deco_time(func):
    func.__doc__+='Decorated by'
    return func


@deco_time
def execute(x,y):
    '''Returned function'''
    return x+y

execute=deco_time(execute)
    
