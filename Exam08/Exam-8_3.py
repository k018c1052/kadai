password = input('入力＞')

if len(password) < 8:
    print('短すぎます')
    pass
elif len(password) >= 13:
    print('長すぎます')
    pass
else:
    print('OK')
    pass
