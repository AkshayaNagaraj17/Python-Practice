f=open("hi.txt","w")
f.write("Heloo\n")
f.writelines(["hi\n","im aksh\n"])
f.close()
f=open("hi.txt","r")
print(f.read())
f.seek(0)
print(f.tell())
print(f.readlines())
f.close()
