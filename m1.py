str=input("Enter a string:  ")
index1=1
index2=3

li=list(str)
li[index1],li[index2]=li[index2],li[index1]


swapped=''.join(li)
print(swapped)
