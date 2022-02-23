# 2/dop. Учитывая целое число n, вернуть true, если оно является степенью двойки. В противном случае вернуть ложь.
# Целое число n является степенью двойки, если существует целое число x такое, что n == 2x.
# Пример 1: Вход: n = 1 | Вывод: правда | Объяснение: 20 = 1
# Пример 2: Вход: n = 16 |Вывод: правда | Объяснение: 24 = 16
# Пример 3: Вход: n = 3 |Вывод: ложь

def isPowerOfTwo(n):
    if n == 1:
        return True
    if n % 2 != 0 or n == 0:
        return False
    return isPowerOfTwo(n / 2)

n = int(input('введите число:'))
print(isPowerOfTwo(n))

# 2ой вариант решения:
from math import log

def degree_two(n: int):
    Logn = log(n, 2)
    if Logn == int(Logn):
        print("True")
    else:
        print("False")
    return Logn

n = int(input('введите число:'))
print(degree_two(n))



