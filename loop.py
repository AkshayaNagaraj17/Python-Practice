
#for loop
ready=input ("Are you ready for the surprise(yes/no):")
if ready =="yes":
    for i in reversed(range(1,4)):
        print(i)
    print("Happy Birthday!!!")
else:
    print("Oops!")
#continue
for a in range (1,11):
    print(a)
    if a==9:
        continue
        #break

#while loop
#1
name=input("Ener the name:")
while name=="":
    print("You didnt entered your  name..")
    name=input("Ener the name:")
print(f"Heloo{name}")

#2
num=int(input("Enter a number from 1 to 10"))
while num<1 or num>10:
    print("Number invalid")
    num=int(input("Enter a number from 1 to 10"))
print(f"Your number is{num} ")

#nested loop

rows=int(input("Enter no of rows:"))
columns=int(input("enter no of columns:"))
symbol=input("Enter the symbol you want:")
for i in range (rows):
    for j in range (columns):
        print(symbol,end=" ")
    print()
