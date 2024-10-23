n=[1,8,4,9,2,3]
k=int(input("k:"))
def small(n,k):
    return sorted(n)[k-1]
print(f"kth smallest is{small(n,k)}")