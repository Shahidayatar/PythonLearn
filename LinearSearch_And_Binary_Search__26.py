# linear search and binary search

#https://www.youtube.com/watch?v=UldZOLylez4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=73
pos=-1
def search(list,n):
    i=0
    while i <len(list):   # we can even do it with while loop
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1 # if you dont incrememnt the loop will run on '5'[list] itself
    return False



list=[9,57,8,4,24,35,]
n=9


if search(list,n):
    print("found at ",pos +1)

else:
    print("not found")


# Binary search
#https://www.youtube.com/watch?v=DE-ye0t0oxE&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=74


def search1(list,n):
    l =0# lower bound
    u=len(list)-1# upper bound

    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1

            else:
                u=mid -1

list=[9,16,38,45,64,99]#  values must be sorted in this type of search
n=96


if search(list,n):
    print("found at ",  pos+1)

else:
    print("not found")

