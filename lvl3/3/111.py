f = open("input.txt")
x = int(f.readline())
f.close()
f2=open("output.txt", "w")
i = 1
while i ** 2 <= x:
    f2.write(str(i**2) + "\n")
    i += 1
f2.close()
