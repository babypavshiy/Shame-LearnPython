import os
import os.path
import time

f=open("1.txt")
x= f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write("list = [5, 4, 3, 2, 1]" + "\n")
f.write(x + "\n")
f.write("f=open('2.txt', 'w')"+ "\n")
f.write("for x in list:" + "\n")
f.write("    f.write(str(x) + '\\n')"+ "\n")
f.write("f.close()"+ "\n")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")
seconds = time.time() - (4)

while os.path.exists("2.txt"):
    time.sleep(0.35)
    os.remove("2.txt")
    

