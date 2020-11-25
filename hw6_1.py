from time import sleep

class TrafficLight:

    def __init__(self):
        self.__color = "black"

    @staticmethod
    def running(count1):
        lightdict = {"red": 7, "yelow": 2, "green": 4}
        lred = ["red","yelow","green"]
        for x in range(0,count1):
         for i in lred:
          print (i)
          sleep(lightdict[i])

traflight = TrafficLight()
print(traflight.running(3))