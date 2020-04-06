# Multi Threading is a complex topic .. google it        # https://stackoverflow.com/questions/2905965/creating-threads-in-python
#https://www.youtube.com/watch?v=GqHLztqy0PU&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=69

# we are trying to run functions at the same time (simultaneous)

from threading import *
from time import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

t1=hello()
t2=hi()

t1.start() # this starts the thread method
sleep(0.2)# we put a gap here so that there is no collision when both the functions executes simulataneously
t2.start()

t1.join()# we wrote this because we are trying to tell the main thread .. let  t1 and t2  thread execute completey then you get executed
t2.join()
print(" bye!")