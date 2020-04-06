
def fibo(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fibo(int(input("enter how many fibonacci number you want")))



                    #   FACTORIAL
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f



result=fact(int(input(" enter the factoiral number : ")))

print(result)