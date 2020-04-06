#https://www.youtube.com/watch?v=Cn7AkDb4pIU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=59
class A:
    def feature1(self):
        print("feature 1 is working")

class B(A):#  to use inheretence in python we dont have extra keyword ,, just  put the super class in bracket
    def feature2(self):
        print("feature 2 is working")

class C():
    def feature3(self):
        print("feature 3 is working")

class D(B,C): # using inheritence of different class
    def feature4(self):
        print("feature 4 is working")

a1=A()
a1.feature1()

b1=B()
b1.feature1()

d1=D()
d1.feature1 ()   # we are accessing class A


# CONSTRUCTOR IN INHERITANCE


class E:
    def __init__(self):
        print("in E")
class F(E):
    def __init__(self):# if you dont put this init it method (i.e constructor) it will call the constructor of E ,, try commenting this
        super().__init__()# but if you want to call both constructor
        print("in F")

f=F()


