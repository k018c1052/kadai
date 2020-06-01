num = int(input('番号＞'))
moji = 'ABCDEFGHIJKLNMOPQRSTUVWXYZ'

if num < 27:
    print(moji[num])
    pass

if num >= 27:
    print(moji[num-27])
    pass
