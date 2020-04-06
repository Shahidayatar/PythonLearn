# try except finally

# in python we have 'except'instead of catch
try:
    x=int(input("enter number 1 "))
    y=int(input("enter number 1 "))
    z= x+y
    k=x/y
    print(z)
    print(k)
except ZeroDivisionError as e:
    print("you got this because the entered number was zero ")
except Exception as e:
    print("enter proper value",e)

finally:
    print(" finally- this is executed always Even if there is an error")# finally is always executed