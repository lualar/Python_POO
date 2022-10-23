import random

class Apple():
    __weigth = 0
    iCount = 0
    tWeight = 0
    
    def __init__(self, weight):
        self.__weigth  = weight
        Apple.iCount += 1
        Apple.tWeight += weight

dApple = {}
for i in range(1000):
    NewAppleWeight = random.uniform(0.2, 0.5)
    if (Apple.tWeight + NewAppleWeight< 300):
        dApple[i] = Apple(NewAppleWeight)

print (Apple.iCount, Apple.tWeight, sep=" -- ")    