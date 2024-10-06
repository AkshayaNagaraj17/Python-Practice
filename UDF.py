n1=input("Enter:")
n2=input("Enter")
s=int(input())
vo=input("Enter vo:")
def con(x,y):
    co=x+y
    print(co)


con(n1,n2)

def sod(di):
    sum=0
    for i in str(di):
        sum=sum+int(i)
    return sum
print("Sod",sod(s))

def vow(c):
    count=0
    a=("a","e","i","o","u")
    for i in c:
        if i in a:
            count=count+1
    print(count)

vow(vo)