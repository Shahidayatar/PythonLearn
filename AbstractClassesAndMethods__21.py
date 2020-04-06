# You cannot create an object or instance of an abstract class

#https://www.youtube.com/watch?v=UDmJGvM-OUw&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=65

from abc import ABC,abstractmethod   # ABC-  abstract base classes
class student(ABC):
    @abstractmethod # if you remove this .. the  code would work
    def games(self):
        print("student class")
class details(student):
    def hello(self):
        print("details class")


#s1=student()# the class is an abstract so there is an error
#s1.details()
s2=details() # this wont work because inherited from abstract class
s2.games()