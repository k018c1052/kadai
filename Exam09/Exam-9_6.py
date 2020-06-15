tango = []

while True:
    moji = input('単語＞')

    if moji not in tango:
        tango.append(moji)
        continue
        pass
    else:
        print(tango,'\n','終了')
        break
