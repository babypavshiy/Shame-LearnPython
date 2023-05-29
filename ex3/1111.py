def task_is_done():
    f=open("privet.txt", 'w')
    f.write("mq")
    f.close()
data = input().split()
message_list = (data[0][0:1], data[1][1:2], data[2][2:3], data[3][2:3], data[4][2:3])
numbers_list = [len(data[0]), len(data[1]), len(data[2]), len(data[3]), len(data[4])]
if (" ".join(message_list) == "1 + 1 = 3" and sum(numbers_list) == 18):
    task_is_done()
    
