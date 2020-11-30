class NewException(Exception):
    def __init__(self,text):
        self.text = text

l=[]
a = input("Enter number: ")
while a != "stop":
 try:
    if a.isdigit():
        l.append(a)
    else:
       raise NewException("Enter number!!!")
 except Exception as err:
     print (err)

 a = input ("Enter number: ")
 if a == "stop":
     break
print(l)