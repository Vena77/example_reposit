file5=open("file5.txt", 'w', encoding="UTF-8")
a = input ("Enter some number:")
file5.write(a)
file5.close()
file5=open("file5.txt", 'r')
a = a.split(" ")
sum = 0
for x in a:
    sum = sum + int(x)
print(sum)    