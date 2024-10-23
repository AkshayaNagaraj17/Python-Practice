di1={}
di2={}
d1=int(input())
d2=int(input())
for i in range(d1):
    key=input("Key")
    value=input("value")
    di1[key]=value
print(di1)
for j in range(d2):
    key=input()
    value=input()
    di2[key]=value   
print(di2)
print(di1|di2)