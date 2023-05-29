f1 = open("input.txt")
x = f1.readlines()
f1.close()
f2 = open("output.txt", "w")
for i in x:
    if int(i)%2==1:
        f2.write(str(int(i)) + "!"+ "\n")
    else:
        f2.write(str(int(i))+ "\n")
f2.close()
