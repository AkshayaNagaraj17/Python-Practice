import os
file=open("helo.txt","w")
file.write("Heloo")
file.writelines(["im aksh\n","im 2o\n"])
file.close()
file=open("helo.txt","a")
file.write("Welcome")
file.close()
file=open("helo.txt","r")
print(file.read())
file.seek(0)
print(file.tell())
print(file.readline())
file.seek(0)
print(file.readlines())

rel="helo.txt"
abs=os.path.abspath(rel)
print(abs)

size=os.path.getsize(rel)
print(size)