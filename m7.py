lm=lambda a,b:a+b

x=int(input())
y=int(input())
print(lm(x,y))

def fun(a,b):
    yield a+b
a=input("a1")
b=input("a2")
print(list(fun(a,b)))

list2=[1,2,3,4]
list1=[7,9,8]
zi=zip(list2,list1)
print(list(zi))

def sq(li1):
    return li1**2
li1=[2,3,4]
map1=list(map(sq,li1))
print(map1)

def fil(map1):
     return map1%2==0
        
f=filter(fil,map1)

print(list(f))