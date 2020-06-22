def max_cd(a,b): 
    if a % b == 0:
        return b
    else:
        return max_cd(a = b,b = a % b)

num1 = int(input('数値1＞'))
num2 = int(input('数値2＞'))

print('最大公約数:',max_cd(num1,num2))
