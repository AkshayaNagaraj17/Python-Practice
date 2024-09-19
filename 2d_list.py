veggies=["brinjal","carrot","onion"]
fruits=["berry","grapes","tomato"]
comp=["mouse","keyboard","monitor"]

#all=[veggies,fruits,comp]
#print(all)
#print(all[0][1])
#print(all[1])

#numpad

numPad=[(1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",0,"#")]
for i in numPad:
    for num in i:
        print(num,end="  ")
    print()