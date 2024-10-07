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
ma=list(map(sq,list1))
print(ma)
#filter

def even(m):
    return m%2==0
        
    

fil=list(filter(even,ma))
print(fil)

lists=[1,23,4,5]
list2=[2,5,6,7]
zi=zip(lists,list2)
print(dict(zi))



def gen(str):
    yield len(str)
    yield str.upper()
str="helo"
print(list(gen(str)))