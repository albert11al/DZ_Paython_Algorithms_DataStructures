# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

def sum_element(num: int):
    num_row = 1
    result = []
    for a in range(0, num):
        if num > 0:
            result.append(num_row)
            num_row = num_row / -2
            num = num - 1
    return result
n = int(input('Количество элементов:'))
print(sum_element(n))
print(f'Сумма элементов {sum(sum_element(n))}')


