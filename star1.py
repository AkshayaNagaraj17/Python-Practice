rows=int(input())
cols=int(input())

for i in range(1,rows):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(rows):
    for k in range(rows-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end=" ")
    print()