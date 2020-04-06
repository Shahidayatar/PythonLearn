class person:

    def __init__(self):         # this is special function
         # https://www.youtube.com/watch?v=WIP3-woodlU&list=RDCMUC59K-uG2A5ogwIrHw4bmlEg&start_radio=1&t=111
        print(" this is a  special inbuilt function .. you dont need to call it .."
              " it will autom atically execute look at'info' we have to call it")

    def info(self):
        print(" Shahid , 19 , Vistula ")

name = person() # THIS IS AN CONSTRUCTOR   #     this says that 'name' is an object of computer
print(type(name))
person.info(name)  # this is the  way you can access 'info'
name.info()
# you can access it directly by using object name


class human:
    def __init__(self,height, name):
        self.height=height#  we are refering to object 
        self.name=name
        print("height is",self.height,'name is ',self.name)
    def body(self):
        print(self.name,self.height)

details=human(190,'shahid')# we have  passed it in the construtor itself

details.body()
