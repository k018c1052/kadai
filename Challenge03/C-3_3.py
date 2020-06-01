import re
moji = input('入力＞')
num = len(re.split('[.!?]', moji))
print(num)
