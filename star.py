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




def inverted_full_pyramid(n):
    # Outer loop for the number of rows
    for i in range(n, 0, -1):
        # Inner loop for leading spaces in each row
        for j in range(n - i):
            print(" ", end="")
        # Inner loop for printing asterisks in each row
        for k in range(2*i - 1):
            print("*", end="")
        # Move to the next line after each row
        print("")

# Set the value of n (number of rows)
n = 5