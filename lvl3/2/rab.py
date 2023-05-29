import os
import time
import os.path

f=open("1.txt")
x=f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write("f = open('input.txt')" + "\n")
f.write("numbers_list = f.readlines()" + "\n")
f.write("f.close()" + "\n")
f.write(x + "\n")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")

while os.path.exists("output.txt"):
    time.sleep(0.4)
    os.remove("output.txt")
