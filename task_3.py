# 3. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import randint

N = 10
a = []
for i in range(N):
    a.append(int(randint(1, 100)) - 50)
print(a)
i = 0
index = -1
while i < N:
    if a[i] < 0 and index == -1:
        index = i
    elif a[i] < 0 and a[i] > a[index]:
        index = i
    i += 1
print('a[%d]=%d' % (index, a[index]))

