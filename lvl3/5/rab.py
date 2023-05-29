import os
import time
import os.path

f=open("1.txt")
x=f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write("def define_word(sign):" + "\n")
f.write("    if sign in 'eyuioaEYUIOA':" + "\n")
f.write("        return 1" + "\n")
f.write("    else:" + "\n")
f.write("        return 0" + "\n")
f.write(x + "\n")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")

while os.path.exists("output.txt"):
    time.sleep(0.4)
    os.remove("output.txt")
