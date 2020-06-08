num = int(input('数値＞'))
x = []
f = True

while f:
    if num / 2 != 0:
        num_2 = divmod(num, 2)
        num = num_2[0]
        x.append(num_2[1])
        pass
    elif num / 2 == 0:
        f = False
    pass

for n in reversed(x):
    print(n,end='')
    pass
