word = ['しりとり']
flag = True

while flag:
    anser = input('答え＞')
    
    if anser[0] in word[-1]:
        for i in word:
            if i in anser:
                print('あなたの負け')
                flag = False
        word.append(anser)
        if anser[-1] in 'ん':
            print('あなたの負け')
            flag = False
    else:
        print('もう一度答えてください')
