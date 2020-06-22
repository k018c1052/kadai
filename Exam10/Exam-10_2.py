bottom = int(input('底辺＞'))
height = int(input('高さ＞'))

def Triangle_area(b,h):
    s = b * h / 2
    return s

print('三角形の面積:',Triangle_area(bottom,height))
