fa_obj = open("newfile.txt", 'w', encoding="UTF-8")
a = input ("Enter something for file:")
while a!="":
    fa_obj.write (a + "\n")
    a = input ("Enter something for file:")
fa_obj.close ()