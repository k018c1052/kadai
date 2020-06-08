num = int(input('数値＞'))
k = 1

for i in range(1,num + 1):
    k *= i
    pass
print(num,'の階乗:',k)