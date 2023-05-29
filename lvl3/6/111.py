def up_vowel(sign):
    if sign in "eyuioa":
        return sign.upper()
    else:
        return sign
f=open("input.txt")
text_list = f.readlines()
f.close()
text_list = [up_vowel(str(i)[:-1]) for i in text_list]
f2=open("output.txt", "w")
f2.write("".join(text_list))
f2.close()
