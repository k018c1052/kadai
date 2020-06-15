year = int(input('西暦＞'))

if year % 4 == 0 and year % 100 != 0:
    print('閏年')
    pass
elif year % 400 == 0:
    print('閏年')
    pass
else:
    print('平年')
    pass
