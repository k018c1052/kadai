n_list = []
num = int(input('数値＞'))

for i in range(1,num + 1):
    if num % i == 0:
        n_list.append(str(i))
        pass
    pass
print(','.join(n_list))
