"""
Q: What is decorator?
A: It is a callable taking in a funciton as parameter and then returning a callable.

Q: What is callable?
A: Any objects that implement __call__ method.
"""
def decorate(original):
    def inner(a, b):
        if b == 0:
            print "We cannot divide a number by 0"
            return 
        else:
            return original(a, b)
    return inner


@decorate
def divide(a, b):
    print a/b

divide(1.0, 2)
divide(1, 0)
