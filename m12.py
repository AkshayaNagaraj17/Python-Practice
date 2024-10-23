def con(a,b):
    return a+b
a=input()
b=input()
print("Concatenation:" ,con(a,b))

def vo(v):
    vow=("a","e","i","o","u")
    vc=0
    for i in v:
        if i in vow:
            vc=vc+1
    print(vc)
v=input()
vo(v)
