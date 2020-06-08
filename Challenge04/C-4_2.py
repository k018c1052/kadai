km = int(input('距離＞'))
price = 200

if km <= 10:
    print(price,'円')
    pass
else:
    km %= 10
    price += km * 20
    print(price,'円')
