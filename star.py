#right-angle triangle
row=int(input("Enter number of rows:"))
column=int(input("enter number of colums:"))

for i in range(1,row+1):
    
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#inverted triangle

for i in range(row+1,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()


