#compound interest calculator
#while loop
#A=P*(1+r/100)pow t
import math
principle=0
interest=0
time=0

while principle<=0:
    principle=float(input("Enter principle:"))
    if principle<=0:
        print("Principle cant be less than 0")

while interest<=0:
    interest=float(input("Enter rate of interest:"))
    if interest<=0:
        print("Interest cant be less than 0")

while time<=0:
    time=int(input("Enter time in years:"))
    if time<=0:
        print("time cant be less than 0")

total=principle* pow((1+interest/100),time)
print(f"Your compound interst will be:{total}2f")


    