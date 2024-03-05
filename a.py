def soluong(a, b):
    a = a
    b = b
    soluong = (a * b)

    return soluong


def luonglamloilon():
    tien_1 = input("tien luong 1: ")
    tien_2 = input("tien luong 2: ")
    return f"Tien 1: {tien_1} \ntien 2:{tien_2}"


tien_1, tien_2 = luonglamloilon()

soluong = soluong(tien_1, tien_2)

print(soluong)