txt=input("Enter a string:  ")

uc=0
lc=0

for i in txt:
    if i.isupper():
        uc=uc+1
    else:
        lc=lc+1
print(uc)
print(lc)