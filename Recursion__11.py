import  sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000) # the default recursion limit is 1000 we changed it
print(sys.getrecursionlimit())


i= 0
def greet():

    global i
    i+=1
    print("hello" , i)
    greet()
greet()


# factorial using recursion

