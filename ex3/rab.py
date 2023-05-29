def task_is_done():
    f=open("res.txt", 'w')
    f.write("1")
    f.close()
f=open("1.txt")
x=f.read()
x=x[:-4]
x=x.split()
f.close()
message_list = (x[0][0:1], x[1][1:2], x[2][2:3], x[3][2:3], x[4][2:3])
numbers_list = [len(x[0]), len(x[1]), len(x[2]), len(x[3]), len(x[4])]
if (" ".join(message_list) == "1 + 1 = 3" and sum(numbers_list) == 18):
    task_is_done()
else:
    f=open("res.txt", 'w')
    f.write("0")
    f.close()  
