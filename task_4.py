# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
N = 10
a = []
for _ in range(N):
    a.append(randint(1, 100))
print(a)
min1 = min(a)
a.remove(min1)
min2 = min(a)
print('1ый минимальный элемент', min1)
print('2ой минимальный элемент', min2)

print('---------------------------------------------------------')

def get_two_min(arr: list) -> tuple:
    min = len(arr)
    sec_min = len(arr)
    for i in arr:
        if i < min:
            sec_min = min
            min = i
        elif i < sec_min:
            sec_min = i

    return min, sec_min

x = [1,2,3,4,0,6]
print(get_two_min(x))