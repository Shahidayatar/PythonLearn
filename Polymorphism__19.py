# there are 4 types of polymorphism
    # 1.Duck typing
    # Operator Overloading
    # 3.Method overloading
    # 4.method Overriding


# 1. Duck typing
class pycharm:
    def execute(self):
        print("working")
        print("duck typing")
class laptop:
    def code(self,ide):
        ide.execute()
ide=pycharm()
lap1=laptop( )
lap1.code(ide)


# this is not from telusko copied from    https://devopedia.org/duck-typing


class Sparrow:
    def fly(self):
        print("Sparrow flying")


class Airplane:
    def fly(self):
        print("Airplane flying")


class Whale:
    def fly(self):# if you chane swim to fly it works (or fly to swim)
        print("Whale swimming")


# The type of entity is not specified
# We expect entity to have a callable named fly at run time
def lift_off(entity):
    entity.fly()


sparrow = Sparrow()
airplane = Airplane()
whale = Whale()

lift_off(sparrow)  # prints `Sparrow flying`
lift_off(airplane)  # prints `Airplane flying`
lift_off(whale)  # Throws the error `'Whale' object has no attribute 'fly'


        # OPERATOR OVERLOADING    https://www.youtube.com/watch?v=9wd50TKv_OQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=63


        # https://www.geeksforgeeks.org/operator-overloading-in-python/        this is extra stuff
x=4
y=5
print(int.__add__(x,y))  # there are many inbuilt functions of int and all data types. click on int and click command
print(int.__ge__(x,y))# gives greater than


class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return  s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

s1 = Student(58,69)
s2 = Student(69,65)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")