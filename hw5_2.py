file1 = open("file1.txt", 'r')
i=0
for a in file1:
    print(a)
    aa = a.split(" ")
    i = i + 1
    print("Кол-во слов в",str(i),"строке:", len(aa))

print("Количество строк в файле:",i)
file1.close()