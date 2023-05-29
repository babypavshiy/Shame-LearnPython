f1 = open("input.txt")
numbers_array = f1.readlines()
f1.close()

numbers_array = [str(int(i)**2)[-1] for i in numbers_array]

f2 = open("output.txt", "w")
f2.write("\n".join(numbers_array))
f2.close()
