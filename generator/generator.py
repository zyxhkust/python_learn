"""
Q: What is generator?
A: A simple way to create iterator

Q: What is the def of generator?
A: A funciton that contains one or more "yield".

Q: What is yield?
A: It is similar to return, but has a littel diff. 
After return, the function complete stopped. 
But after implementing yield, the funciton will be suspended temporarily, and start the folloing process on the next call.
"""

def func1(n):
    n -= 1
    yield n

    n -= 1
    yield n

def call_func1():
    temp = func1(2)
    for res in temp:
        print res

call_func1()

