import time

mtime=int(input("Enter time in seconds : "))

for i in range( mtime , 0 ,-1): #-1 is counting backwards
    sec=i%60    #if time goes above 60
    min=int(i/60)%60
    hour=int(i/3600)
    print(f"{hour:02}.{min:02}.{sec:02}")
    
    time.sleep(1)

print("Time's up")