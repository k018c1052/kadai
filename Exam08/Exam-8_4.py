point = int(input('入力＞'))

if point >= 80:
    print('評価：優')
    pass
elif point < 80 and point >= 70:
    print('評価：良')
    pass
elif point < 70 and point >= 60:
    print('評価：可')
    pass
elif point < 60:
    print('評価：不可')
    pass
