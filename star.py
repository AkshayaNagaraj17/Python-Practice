#right-angle triangle
row=int(input("Enter number of rows:"))
column=int(input("enter number of colums:"))
print("Right-angle triangle")
for i in range(1,row+1):
    
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
#inverted triangle
print("Inverted triangle")
for i in range(row,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(row):
    for k in range(row-i-1):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=' ')
    print()