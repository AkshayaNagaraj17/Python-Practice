lam=lambda a,b :a+b
print(lam(2,3))
#map
def sq(num):
    return num**2
n=int(input())
list1=[]
for i in range(n):
    ele=int(input("enter"))
    list1.append(ele)
ma=map(sq,list1)
print(list(ma))
#filter

def even(m):
    if m%2==0:
        return True
    
n=int(input())
list1=[]
for i in range(n):
    ele=int(input("enter"))
    list1.append(ele)
fil=filter(even,list1)
print(list(fil))

lists=[1,23,4,5]
list2=[2,5,6,7]
zi=zip(lists,list2)
print(dict(zi))



def gen(str):
    yield len(str)
    yield str.upper()
str="helo"
print(gen(str))