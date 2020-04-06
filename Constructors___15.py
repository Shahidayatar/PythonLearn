#https://www.youtube.com/watch?v=ic6wdPxcHc0&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=55

class computer :             # if you want to keep the class empty then use 'pass'
    def __init__(self):
        self.name= 'shahid'        # we are making variables
        self.age= 19
        print(self.name, self.age)

    def update(self):
        self.age=27


    def compare(self,c2):  # compare take two parameter   compare(who is calling, whom to compare )
        if self.age==c2.age:
            return  True
        else:
            return  False


c1=computer()    # constructor calculates size of the memory
#c1.update() if you put this age will refer to update function
c2=computer()

if c1.compare (c2):# compare is not inbuild function # this is the way you compare
    print("the age is same ")
else:
    print("the age is different")

c1.update()# because of this c1.age refers to 27


print('name is ',c1.name,'and age is ',c1.age)




# another example of compre

class person:
    def __init__(self):
        self.age=92
    def info(self):
        self.age=23
    def comparing(self,p2):
        if p1.age==p2.age:
            print("its correct")
        else:
            print("not correct")



p1=person()

#p1.info()  # this will change the value of  age remove comment to see
p2=person()

if p1.comparing(p2):
    print("this is an compare example")
else:
    print(" you get it !")

