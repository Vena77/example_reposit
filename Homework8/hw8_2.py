class NewException(Exception):
    def __init__(self,text):
        self.text = text

def delenie(a,b):
    if not b:
      raise NewException("Делить на ноль нельзя!")
    return a/b

try:
   print(delenie(5,0))
except Exception as err:
    print(err)