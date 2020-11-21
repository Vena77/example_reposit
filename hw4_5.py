from functools import reduce

def ff(a,b):
 return a*b

list =[x for x in range(100,1001) if x%2==0]
print(list)
print(reduce(ff, list))
