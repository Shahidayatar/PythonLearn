class car:   # https://www.youtube.com/watch?v=lVfGQOzzRCM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=57
    wheels=4 # class variable
    def __init__(self):
        self.comapany= "BMW"# these are instance variable
        self.model="A3"
        self.mileage=12

c1=car()
c2=car()
print(c1.comapany,c1.model,c1.comapany) # model is used by both objects'C1' and 'C2'
c1.comapany= "mercedes"
print(c1.comapany)

# if we want  to call the class  variable
print(c1.wheels)
print(c2.wheels)
#but if you want to change the value of wheels for all objects we need to call the class.

car.wheels=12
print(c1.wheels)
print(c2.wheels)




#         types of Methods
 #three types of methods 1.Instance methods 2. class methods , 3. Static method


class student:

    school= 'vistula'
    def __init__(self,age,name):# instance methods       # when you put an argument .. you need to insert the value in the when you call it
        self.age=age
        self.name=name

       # below is function for clas method

    @classmethod
    def info(cls):
        print(cls.school)


          # below is function for clas method
    @staticmethod
    def details():
        print("its static method")



s1=student(22,'shahid')
s2=student(31,'sofiya')
print(s1.age)

print(student.info())


print(student.details())

