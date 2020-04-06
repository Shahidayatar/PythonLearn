#factorial using recursion
def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)
result=fact(3)
print( result)




                       #               Anonymous functions or Lambda functions

# [these are functions with no name . it is  used only when there one line of code or samll codeor less express]

# findig a square of a number
s= lambda s:s*s
# you always need to assign it to someone i.e s=......
results= s(5)
print(results)


# another example
a= lambda a,b:a*b
ans=a(9,4)
print(ans)



  