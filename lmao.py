def soluong(a, b):
    a = a
    b = b
    soluong = (a * b)

    return soluong


def luonglamloilon():
    tien_1 = input("tien luong 1 cua Hung: ")
    tien_2 = input("tien luong 2 cua Hung: ")
    return tien_1, tien_2


tien_1, tien_2 = luonglamloilon()

soluong = soluong(tien_1*100, tien_2*100)

print(soluong)
