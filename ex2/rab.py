def task_is_done():
    f=open("res.txt", 'w')
    f.write("1")
    f.close()
f=open("1.txt")
x=f.read()
x=x[:-4]
x=x.split()
f.close()
x = [ x[0][0:2], x[1][0:2], x[2][2:4], x[3][2:4] ]
if ("".join(x) == "password"):
    task_is_done()
else:
    f=open("res.txt", 'w')
    f.write("0")
    f.close()
