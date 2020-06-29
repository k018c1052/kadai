from Dice import Dice

while True:
    a, b, c = Dice(6), Dice(6), Dice(6)
    s = [a.roll(), b.roll(), c.roll()]
    print(s)

    if s.count(s[0]) == 3:
        print('当たり！')
        break

