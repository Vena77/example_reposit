class Road:
 massa = 25

 def __init__(self,lenght,width):
       self._lenght = lenght
       self._width = width


 def  count_massa_asfalt(self,tolshina):
    return self._lenght * self._width * tolshina * self.massa

road = Road(1000, 50)
print("Asfalta nado:",road.count_massa_asfalt(3))