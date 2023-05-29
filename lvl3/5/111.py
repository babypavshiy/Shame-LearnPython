def define_word(sign):
    if sign in "eyuioaEYUIOA":
        return 1
    else:
        return 0
f=open("input.txt")
x = f.readlines()
x = [str(i)[:-1] for i in x]
f.close()
f2 = open("output.txt" , "w")
for i in x:
    f2.write(str(define_word(i)) + "\n")
f2.close()
