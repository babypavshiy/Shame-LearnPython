import os
import time
import os.path

f=open("1.txt")
x=f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write("f1 = open('input.txt')" + "\n")
f.write("numbers_array = f1.readlines()" + "\n")
f.write("f1.close()" + "\n")
f.write(x + "\n")
f.write('f2 = open("output.txt", "w")' + "\n")
f.write('f2.write("\\n".join(numbers_array))' + "\n")
f.write("f2.close()")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")

while os.path.exists("output.txt"):
    time.sleep(0.4)
    os.remove("output.txt")
