
# bubble sort
#https://www.youtube.com/watch?v=Vca808JTbI8&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=75
def sort(nums):

    for i in range(len(nums)-1,0,-1):# sort means arrange numbers from lower to higher
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]# here we are swapping variables
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums = [5, 3, 8, 6, 7, 2,444,35,]#we arrange this series from lower to higher
sort(nums)

print(nums)


  # Selection sort


def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)