"""
Q: What is closure?
A: It must satisfy 3 criterion:
    1. You must have nested function
    2. The nested function must refer to a value defined in the enclosing function
    3. The enclousing function must return the nested function
"""

def enclosing(msg):
    def nested():
        print msg
    return nested

fun = enclosing("nested function")
fun()

"""
Q: When to use it?
A:  1. It provides some form of data hiding
    2. It can take place of a class when the number of class methods is small
"""