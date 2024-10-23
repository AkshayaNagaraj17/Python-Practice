with open("numbers.csv","r") as file:
    for i in file:
        numbers=list(map(int,i.strip().split(",")))
        print(numbers)