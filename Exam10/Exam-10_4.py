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
    print('平均:',sum_n(a) / len(n_list))

def max_n(m):
    nu_list = num.split(' ')
    print('最大値:',max(nu_list))

#print('合計:',sum_n(num))
average(num)
max_n(num)