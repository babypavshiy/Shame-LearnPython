import os
import os.path
import time
f=open("1.txt")
x= f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write(x + "\n")
f.write("f=open('2.txt', 'w')"+ "\n")
f.write("for x in cube_list:" + "\n")
f.write("    f.write(x + '\\n')"+ "\n")
f.write("f.close()"+ "\n")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")

while os.path.exists("2.txt"):
    time.sleep(0.35)
    os.remove("2.txt")
        
