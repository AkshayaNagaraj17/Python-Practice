#Rectangle of area 

l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
area=l*b
#for super script numlock+alt+0178
print(f"The area of rectangle: {area}cm²")

 #shopping cart
item=input("Enter the item:")
price=int(input("Enter the price:"))
quantity=int(input("Quantity:"))
print(f"You bought{quantity}{item} on {price}")
total=quantity*price
print(f"Your grand total is:{total}")