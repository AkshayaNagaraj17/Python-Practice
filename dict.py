capital={"India":"Delhi","china":"Beijing","Russia":"Moscow"
}
print(capital.get("India"))
capital.update({"India":"Chennai"})
print(capital)
capital.pop("Russia")
print(capital)
#capital.clear()
#print(capital)
keys=capital.keys()
for i in keys:
    print(i)
item=capital.items()
#print(item) displays in tuple
for keys,value in item:
    print(f"{keys}:{value}")

#Exercise

menu={"Pizza":190,"Soda":100,"Brownie":120,"Burger":200,"Icecream":150}
cart=[]
total=0
print("Menu.........")
item=menu.items()
for keys,value in item:
    print(f"{keys:10}:{value}")
while True:
    food=input("Enter food (q to quit:)").lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total=total+menu.get(food)
    print(food)