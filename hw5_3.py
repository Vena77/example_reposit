file2 = open("file2.txt", 'r')
sps=[]
sum = 0
i = 0
a = file2.readline()
while a:
 aa = a.split(" ")
 if int(aa[1])<20000:
    sps.append(aa[0])
 sum = sum + int(aa[1])
 i = i+1
 a = file2.readline()
 if not a:
        break
print("Surname who have earn less 20000:",sps)
print("Sred.velichina dohoda sotrudnicov:",sum/i)
file2.close()

