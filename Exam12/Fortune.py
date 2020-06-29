import random as r

class Fortune():
    def draw(self):
        unsei = ['大吉', '中吉', '小吉', '凶', '大凶']
        num = r.randint(0,4)
        print(unsei[num])
