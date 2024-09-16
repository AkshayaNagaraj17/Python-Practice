#if statement
name=input("Enter your name:")
if name=="":
    print("You didnt yet entered your name!")
else:
    print(f"Heloo {name}...")

# simple calculator program

n=int(input("Enter first number:"))
m=int(input ("Enter first number:"))
operator=input("Give the operator(+,-,*,/):")
if operator=="+":
    print(f"Addition:{n+m}")
elif operator=="-":
    print(f"Subtraction:{n-m}")
elif operator=="*":
    print(f"Multiplication:{n*m}")
elif operator=="/":
    print(f"Division:{n/m}")
else:
    print("Nothing happened")

#conditional expression ternary operator
#one line code
num=5
print("Positive "if num>0 else "Negative")


#while loop

name=input("Ener the name:")
while name=="":
    print("You didnt entered your  name..")
    name=input("Ener the name:")
print(f"Heloo{name}")
