def fact(a):
    i=1
    v=1
    while i<a+1:
        v= v*i
        i+=1
        yield v

n=input("Enter n:")
listn = [el for el in fact(int(n))]
print(listn)

