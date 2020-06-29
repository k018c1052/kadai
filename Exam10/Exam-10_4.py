num = input('数値＞')

def sum_n(n):
    num_list = n.split(' ')
    s = 0
    for i in num_list:
        s += int(i)
        pass
    return s

def average(a):
    n_list = a.split(' ')
    return sum_n(a) / len(n_list)

def max_n(m):
    nu_list = m.split(' ')
    return max(nu_list)


#print('合計:',sum_n(num))
print('平均:', average(num))
print('最大値:', max_n(num))
