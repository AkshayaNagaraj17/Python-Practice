str=input("Enter a string:  ")
index1=1
index2=3

li=list(str)
li[index1],li[index2]=li[index2],li[index1]


swapped=''.join(li)
print(swapped)

s1=input()
s2=input()

n1=s1[:2]+s2[2:]
n2=s2[:2]+s1[2:]
print(n1,"",n2)