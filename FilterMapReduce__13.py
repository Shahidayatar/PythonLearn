# we can do it using normal fun .. but we are using lamda
from functools import reduce
#         https://www.youtube.com/watch?v=kj850Y8y8FI&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=47
nums= [2,4,4,5,6,7,8,5,4 ]
evens=list(filter(lambda n:n%2==0,nums ))        # filter takes two arguments 1. function and 2. iteration [thing to iterate
print(evens) # we got all even number

doubles=list(map(lambda n:n*2,evens))            # map is usually used to change values/
print(doubles)


sum=reduce(lambda a,b:a+b,doubles)              # to use reduce we need to import it.. used to return 1 value
print(sum)





      #             DECORATOR

#In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

# using decorator we can add extra features to a function

#https://www.youtube.com/watch?v=yNzxXZfkLUA&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=48
def div(a,b):
   print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div= smart_div(div)
div(2,6)


            #       MODULES
# we will call other file function over  here

#https://www.youtube.com/watch?v=1RuMJ53CKds&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=49

from FactorialUsingRecursion__12 import *

fact(3)


      # https://www.youtube.com/watch?v=pzNISmtmzcY&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=50
print("hello "+__name__) # __name__ is a special variable  it is not defined it is inbuilt  # we are evem using import but we have not done it
                        # in the video
