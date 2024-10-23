f=open("hi1.txt","w")
f.write("heloo\n")
f.write("heloo everyone\n")
f.close()
f=open("hi1.txt","r")
text=f.read()
print(text)
freq={}
words=text.split()
for w in words:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1
for w ,fr in freq.items():
    print(f"{w}:{fr}")
f.close()