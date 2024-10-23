#1
prices=[1,9,2,11,1,9,2]
min_pro=1
max_pro=0
for price in prices:
    min_pro=min(min_pro,price)
    profit=price-min_pro
    max_pro=max(max_pro,profit)
print("Max Profit: ",max_pro)

#2
