array = [5, 4, 3, 2, 1]
array.reverse()
array[0]*=3
array[1]*=3
array[2]*=3
array[3]*=3
array[4]*=3
f = open("1.txt", "w")
for x in array:
    f.write(str(x) + "\n")
f.close()
