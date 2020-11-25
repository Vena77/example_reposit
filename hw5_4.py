dict1={"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
file3 = open("file3.txt", 'r')
file4 = open("file4.txt", 'w', encoding="UTF-8")
a = file3.readline()
while a:
 word = a.split(' ')
 file4.write(dict1[word[0]]+" - "+word[2]+"\n")
 a = file3.readline()
 if not a:
  break
file3.close()
file4.close()