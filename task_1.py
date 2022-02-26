# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def mult_num():
    result = {}
    for n in range(2, 10):
        result[n] = []
        for i in range(2, 100):
            if i % n == 0:
                result[n].append(i)
        print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')

mult_num()

print('----------------------------------------------------')

for i in range(2, 10):
    num = 99//i
    print(f'Для числа {i} кратны - {num}')

