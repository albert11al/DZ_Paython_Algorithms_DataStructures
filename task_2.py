# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

def min_max(num: int):
    a = []
    for _ in range(num):
        a.append(randint(1, 100))
    min = a[0]
    max = a[0]
    for i in a:
        if i < min:
            min = i
        elif i > max:
            max = i
    print('Максимальный элемент: arr[%d]=%d. Минимальный элемент: arr[%d]=%d'
          % (a.index(max), max, a.index(min), min))
    print('до замены местами:', a)
    inmim = a.index(min)
    inman = a.index(max)
    a[inmim] = max
    a[inman] = min
    print('после замены местами:', a)
num = int(input('введите количество элементов в масcиве: '))
min_max(num)

print('-----------------------------------------------------------')

def snap_min_max(array: list):
    mn = 0
    mx = 0
    for i in range(1, len(array)):
        if array[i] > array[mx]:
            mx = i
        elif array[i] < array[mn]:
            mn = i

    array[mn], array[mx] = array[mx], array[mn]

arr = [4, 5, 25, 6, 0, 1]
print(arr)
snap_min_max(arr)
print(arr)