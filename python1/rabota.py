import os
import os.path
import time
f=open("qq.txt")
x= f.read()
f.close()
f=open("qq.txt",'w')
f.write(x + "\n")
f.write("f=open('textik.txt', 'w')"+ "\n")
f.write("f.write(text)"+ "\n")
f.write("f.close()")
f.close()
os.rename('qq.txt', 'qq.py')
os.system('"qq.py"')
os.remove("qq.py")

while os.path.exists("textik.txt"):
    time.sleep(0.4)
    os.remove("textik.txt")
