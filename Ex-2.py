#if statement
name=input("Enter your name:")
if name=="":
    print("You didnt yet entered your name!")
else:
    print(f"Heloo {name}...")

#calculator program

n=int(input("Enter first number:"))
m=int(input ("Enter first number:"))
operator=input()
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