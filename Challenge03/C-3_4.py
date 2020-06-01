s = '0123456789ABCDEF'
ip_10 = input('入力>')
x = ip_10.split('.')

num1, num2, num3, num4 = int(x[0]), int(x[1]), int(x[2]), int(x[3])
num1_16 = divmod(num1, 16)
num2_16 = divmod(num2, 16)
num3_16 = divmod(num3, 16)
num4_16 = divmod(num4, 16)

ip_16 = s[num1_16[0]] + s[num1_16[1]] + ':'
ip_16 += s[num2_16[0]] + s[num2_16[1]] + ':'
ip_16 += s[num3_16[0]] + s[num3_16[1]] + ':'
ip_16 += s[num4_16[0]] + s[num4_16[1]]
print(ip_16)
