def name():#this is the structure of function
    print("this is the structure of function ")
# this function wont run if you dont call it
name()
name()# we can call it multiple times

# add number using function by taking parameters

def add(x,y):
    z=x+y
    return z

result = add(4,5)
print(result)

# watch telusko python video 33 #https://www.youtube.com/watch?v=ijXMGpoMkhQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=37

def update(x):
    x=8
    print(x)
update(10)# look at the difference in ouput we updated it



def person(name,age):
    print(name,age)
person( age = 32,name = "shahid" )# we should assign the name first but we specified the age first


#    very important

def calculator(x,*y):# the star tells that y can have multiple values
    print(x)
    print(y)

    z=x

    for i in y:
         z=z+i

    print(z)


calculator(3,4,5,6,7)