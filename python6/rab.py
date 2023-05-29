import os
import time
import os.path

f=open("1.txt")
x=f.read()
x=x[:-4]
f.close()
f=open("1.txt",'w')
f.write("def object_in_range(a):" + "\n")
f.write("    if a == 'pico' or a == 'kristi' or a == 'Kristi':" + "\n")
f.write("        return True" + "\n")
f.write("    else:" + "\n")
f.write("        return False" + "\n")
f.write("def change_door_status_to(i):" + "\n")
f.write('    if i.lower() == "open":' + "\n")
f.write("        list.append(1)" + "\n")
f.write("    else:" + "\n")
f.write("        list.append(0)" + "\n")
f.write("list = []" + "\n")
f.write(x + "\n")
f.write("f=open('2.txt','w')" + "\n")
f.write("f.write(str(list[-1]))")
f.close()
os.rename('1.txt', '1.py')
os.system('"1.py"')
os.remove("1.py")
seconds = time.time() - (4)

while os.path.exists("2.txt"):
    time.sleep(0.40)
    os.remove("2.txt")
    

