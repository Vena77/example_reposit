file = open("doc2.txt", 'r')
dict1={}
a = file.readline()
i = 0
sum = 0
while a:
 aa = a.split(" ")
 prib = int(aa[2])-int(aa[3])
 dict1[aa[0]]=prib
 if prib>0:
     sum = sum + prib
     i = i+1
 a = file.readline()
 if not a:
        break
sum = sum/i
list1=[dict1,{"average_profit":sum}]
file.close()

import json
with open("file_json.json",'w') as json_obj:
     json.dump(list1,json_obj)
