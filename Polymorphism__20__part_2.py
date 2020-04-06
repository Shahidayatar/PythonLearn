# method overloading and overdding

# https://www.youtube.com/watch?v=CcTzTuIsoFk&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=64

    # method overloading
class student:
    def add(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s= a+b
        else:
            s=a
        return s

s1=student()
print(s1.add(3))# none is used to eneter how many argumnets you would like to enter



#Method overrirding


class human:
    def show(self):
        print("method overloading")
class person(human):
    def show(self):# if you  dont have a show here it will overiride and print the show of human becuse human is  parent of it
        print("we are learning")

p1=person()
print(p1.show())