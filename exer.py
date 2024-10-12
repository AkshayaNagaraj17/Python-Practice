n=int(input("Enter a num"))
for i in range(1,n):
    if n%i==0:
        print(i)

for i in range(1000,2000):
    if (i%11==0 and i%6 !=0):
        print(i)
sq={}
for i in range(n):
    sq[i]=i**2
print(sq)

sqr={i:i**2 for i in range(1,n)}

h="cat","aksh","dee","ti"
print(list(h))
print(tuple(h))
print(sorted(h))

list=["cat","dog","pooop"]
sqq={}
for i in list:
    sqq[i]=len(i)
print(sqq)