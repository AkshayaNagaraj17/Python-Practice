n=[1,2,3,4,5]
target=int(input("Enter:"))
found=False
for i in range(len(n)):
    if n[i] ==target:
        print(f"{target} at{i}")
        found=True
        break
if not found:
    print("not found")