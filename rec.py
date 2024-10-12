def pow(b,e):
    if e==0:
        return 1
    if e>0:
        return b*(pow(b,e-1))
n=int(input())
m=int(input())
print(pow(n,m))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
a=int(input())
print("Fact",fact(a))

def fibo(f):
    if f < 0:
        print("No")
    elif f == 0:
        return 0
    elif f == 1 or f == 2:
        return 1
    else:
        return fibo(f-1)+fibo(f-2)
n1=int(input())
for i in range(n1):
    print(fibo(i),end=" s")