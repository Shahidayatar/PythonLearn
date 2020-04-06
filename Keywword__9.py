def person(name,*data):
    print(name)
    print(data)
person("shahid",4,"sdhs",42)



# suppose assing the parameter while printing
def person1(name,**data):
    print(name)
    print(data)
person1("adil", city= "mumbai",age=28)  # look at the difference



    #  Global and local varable

num=10
def number ():
    num=9
    print(num)


number()# similar, if you want to access global variable i.e 10 you use global, look at the difference the code above and below

num1=19
def number1():
    global num1
    print(num1)
number1()# the concept of globals() is not disscussed you look here.. it has something to with id
        #https://www.youtube.com/watch?v=QYUbLevwgDQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=40    (6.30 min)


def oddeven (lst):# to find number of odd and even from the list

        even = 0
        odd = 0
        for i in lst:
            if i%2==0:
                even+=1
            else:
                odd+=1
        return even, odd

lst = [9, 4, 5, 6, 3, 2, 1, 414, 4, 5, 5]
even , odd = oddeven( lst )

print(even, " :   even count") # will print odd and even
print(odd, " :   odd count")



