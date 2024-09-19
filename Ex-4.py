#shopping cart

food_items=[]
prices=[]
total=0

while True:
    food=input("Enter a food (q to quit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price for {food}:"))
        food_items.append(food)
        prices.append(price)

print("....Your cart....")
print()
for i in food_items:
    print(i,end=" , ")
for j in prices:
    total=total+j
    print()
print("Your total : ",total)