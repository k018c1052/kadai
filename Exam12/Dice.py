import random as r

class Dice():
    def __init__(self,num):
        self.num = num
        
    def roll(self):
        return r.randint(1, self.num)