uf = int(input('上底＞'))
bottom = int(input('下底＞'))
height = int(input('高さ＞'))

def Triangle_area1(u, h):
    s = u * h / 2
    return s

def Triangle_area2(b, h):
    s = b * h / 2
    return s

def Trapezoid_area():
    print('台形の面積:', Triangle_area1(uf, height) + Triangle_area2(bottom, height))

Trapezoid_area()
