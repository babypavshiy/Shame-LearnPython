def task_is_done():
    f=open("privet.txt", 'w')
    f.write("mq")
    f.close()
f=open("mama.txt")
x=f.read().split()
x[0] = int(x[0])
x[1] = len(x[1])
x[2] = int(x[2])
x[3] = len(x[3])
#data = input().split()
#numbers = [ int(data[0]), len(data[1]), int(data[2]), len(data[3]) ]
if (sum(x) == 12):
    task_is_done()

