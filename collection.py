#used to store multiple values
#list=>[]  orderd accepts dupplicates changeable
#set => {} unordered add remove ok no duplictes
#tuple=>() ordered unchangeable duplictes ok

fruits=["apple","orange","grapes"]
fruits[2]="lemon"
#print(help(fruits))
fruits.append("pineapple")
fruits.sort()
print(f"Asc order{fruits}")
fruits.reverse()
print(f"desc order:{fruits}")


#set

games={"cricket","tennis","bat"}
print("bat" in games)
games.add("football")
print(games)
games.remove("cricket")
print(games)

#tuple

name=("aksh","eleven","sid")
print(name.index("aksh"))
