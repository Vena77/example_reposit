pr_dict ={}
file6=open("doc11.txt", 'r')
a = file6.readline()
while a:
 zz = a.split(' ')
 i=1
 while i<=len(zz)-1:
    num = ""
    for x in zz[i]:
       if x!="(":
         num = num + x
       else:
         break
    zz[i]=num
    i=i+1
 sum = 0
 j=1
 while j<=len(zz)-1:
    if zz[j].isdigit():
      sum = sum + int(zz[j])
    j=j+1
 pr_dict[zz[0][:len(zz[0])-1]] = sum
 a = file6.readline()
 if not a:
  break
print(pr_dict)
file6.close()
