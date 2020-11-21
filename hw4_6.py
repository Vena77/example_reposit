from itertools import count,cycle
from time import sleep

for x in count(3):
  print(x)
  sleep(1)
  if x>9:
   break

xx=[1, 2, 3]
i=0
for a in cycle(xx):
  print(a)
  sleep(1)
  i=i+1
  if i>10:
   break