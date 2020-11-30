from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def consumpt(self):
       pass

class Coat(Clothes):
    def __init__(self,size):
       self.size = size

    @property
    def consumpt(self):
       return self.size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self,tall):
        self.tall = tall

    @property
    def consumpt(self):
       return 2 * self.tall + 0.3

def consumptAll(lc,ls):
    sum_coat = 0
    sum_suit = 0
    for el in lc:
       sum_coat=sum_coat+coat.consumpt*el
    for el in ls:
       sum_suit=sum_suit+suit.consumpt*el
    return sum_coat+sum_suit

lcoat=[10,2,56,77,100]
lsuit=[33,9,8,2,3]
coat = Coat(52)
suit = Suit(172)
print(consumptAll(lcoat,lsuit))
print(coat.consumpt)
print(suit.consumpt)


