def Factorial(n):
    if n > 1:
        return n * Factorial(n - 1)
    return 1

num = int(input('数値＞'))
print('階乗:',Factorial(num))
