
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
        break
    else:
        print(a)
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