year = int(input('西暦＞'))

if (year - 1896) % 4 == 0 and year >= 1896:
    print('開催年です')
    pass
else:
    print('開催年ではありません')
    pass
