
list = [x for x in range(2,300,20)]
i = 0
while i<len(list):
  list[i],list[i-1] = list[i-1],list[i]
  i = i + 2
print(list)
# создали нужный список

nlist =[list[el] for el in range(1,len(list)) if list[el-1] < list[el]]
print(nlist)