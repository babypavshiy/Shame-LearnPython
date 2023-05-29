def task_is_done():
    f=open("res.txt", 'w')
    f.write("1")
    f.close()
f=open("1.txt")
x=f.read()
x=x[:-4]
x=x.split()
f.close()
x[0] = int(x[0])
x[1] = len(x[1])
x[2] = int(x[2])
x[3] = len(x[3])
if (sum(x) == 12):
    task_is_done()
else:
    f=open("res.txt", 'w')
    f.write("0")
    f.close()
