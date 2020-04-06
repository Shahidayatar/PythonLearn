# iterators
nums=[2,4,7,9]
for i  in nums:# this is one way of printing it
   print(i)
    # lets try with iterators
it= iter(nums)
print(it.__next__()) # this will only print one value
print(next(it))# even you can do this way.. this would print  the second value

class poland:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=7:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration  # this is an exception
values=poland()
for i in values:
    print(i)
      #Generators# yield keyword
def topten():

    yield 11  # yield is similar to return but we can have mutliple yeild but not multiple return
    yield 12 # in return you cannot write code  below it but  in yield you can
    yield 13

    n=1
    while n<=5:
        sq= n*n
        yield sq #return terminates the  function
        n+=1


ans=topten()
print(ans.__next__())
for i  in ans:
    print(i)

