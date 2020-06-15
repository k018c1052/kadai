num = int(input('数値>'))
n_list = []

for i in range(1,num + 1):
    if i % 3 == 0 and i % 5 == 0:
        n_list.append('FizzBuzz')
        pass
    elif i % 3 == 0:
        n_list.append('Fizz')
        pass
    elif i % 5 == 0:
        n_list.append('Buzz')
        pass
    else:
        n_list.append(str(i))
    pass
pass
print(','.join(n_list))
