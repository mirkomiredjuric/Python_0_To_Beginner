
#global constants
PI = 3.141592653589793 #all global constants to UPPER CASE

i = 50


def foo():
    i = 100 #local variable inside of def
    return i


foo() #call foo() but we don't save value of i from foo()
print(i) #prints global variable, which is still 50