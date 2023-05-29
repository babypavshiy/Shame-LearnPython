f=open("1.txt")
x= f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write(x)
f.close()
