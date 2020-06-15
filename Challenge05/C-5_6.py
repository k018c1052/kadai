num = int(input('数値＞'))

def so(n):
    if n <= 1:
        return '素数ではありません'

    if n == 2:
        return '素数です'

    for i in range(3,n,2):
        if n % i == 0:
            return '素数ではありません'
    return'素数です'

print(so(num))