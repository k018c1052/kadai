cm = int(input('身長＞'))
kg = int(input('体重＞'))
m = cm / 100
bmi = kg / (m * m)

if bmi < 18.5:
    print('痩せ過ぎ')
    pass
elif bmi >= 18.5 and bmi < 25:
    print('標準')
    pass
elif bmi >= 25:
    print('肥満')
    pass
