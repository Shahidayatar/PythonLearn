
#https://www.youtube.com/watch?v=b7JzgybKvys&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=58
class student:


    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name, self.age)


s1= student("shahid",22)
s2=student("adil ",19)
print(s1.show()) # if you   want to get all details of s1 , create a function(show) and call it later
print(s2.show())




# second code

class human:
    def __init__(self, name, height):
        self.name=name
        self.height=height
        self.per=self.person()# you called the person class here and later on you can access it from here



    class person:
        def __init__(self):
            self.color='white'
            self.age=21
        def show(self):
            print(self.color,self.age)


h1=human("shahid", 163)

print(h1.per.age)# this is way to access the inner class (person)



h1.per.show()# you can even access all details at same time this way