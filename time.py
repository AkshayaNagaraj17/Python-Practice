import time

def time1(start,end):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Time over!")
time1(0,10)