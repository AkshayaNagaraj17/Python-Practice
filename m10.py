n=5
l1=[]
for i in range(n):
    el=int(input())
    l1.append(el)
ec=0
oc=0
for i in l1:
    if i%2==0:
        ec=ec+1
    else:
        oc=oc+1
print(ec)
print(oc)