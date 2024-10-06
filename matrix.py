rows=int(input("Enter rows:"))
cols=int(input("Enter colums:"))

matrix=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        el=int(input(f"the num at{i} {j}:"))
        row.append(el)
    matrix.append(row)

for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j<=i:
            print(matrix[i][j],end=" ")
        else:
            print("0",end=" ")
    print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j>=i:
            print(matrix[i][j],end=" ")
        else:
            print("0",end=" ")
    print()
for i in range(len(matrix)):
    print(matrix[i][i],end=" ")
print()
for i in range (len(matrix)):
    print(matrix[i][rows-1-i],end=" ")
print()