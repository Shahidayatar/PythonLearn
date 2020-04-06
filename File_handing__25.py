#https://www.programiz.com/python-programming/file-operation



o=open('shah','r')# this file is already created before # 'r' denotes that file is read only
print(o)
# print(o.read())# this is used to read data from the file     ( we have commented this line because we want to copy the data in  below code)
# print(o.readline())# will onlu print one line fro the file  ( if you want to see the output remove comment and see in the console

o1=open('auto-created','w')
o1.write("hello . this  file which we created below we are gonna copy data from other file into this  (from'shah')" )

o1=open('auto-created','a')# 'a' denotes append ..
o1.write("this is added ")

# we will copy data from 'shah ' and paste it in auto_created

for data in o:
    o1.write(data)


# now we are gonna copy an image
f= open('python-array-supported-type-code.png','rb')# rb in read binary

f1= open('my image.jpg','wb')# wb is write binary  # we have created this image and copied the image from above into this
for i in f:
     f1.write(i)