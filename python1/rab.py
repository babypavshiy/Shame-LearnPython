import os
f=open("1.txt")
x= f.read()
x=x[63:-4]
f.close()
f=open("name.txt",'w')
f.write(x)
f.close()
os.remove("1.txt")

