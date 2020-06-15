word = ['しりとり']

while True:
    anser = input('答え＞')
    
    if word in []:
        word.append(anser)
    elif anser[0] in word[-1][-1]:
        for i in word:
            if i in anser:
                print('あなたの負け')
                break
        word.append(anser)
    else:
        print('もう一度答えてください')

    if anser[-1] in 'ん':
        print('あなたの負け')
        break
