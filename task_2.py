# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# 1ый вариант решения:
def natur_num(num: str):
    even = 0
    not_even = 0
    for i in num:
        if int(i) % 2 == 0: #Если число делится без остатка на 2, его последняя цифра четная
            even += 1       # Увеличиваем на 1 счетчик четных цифр even
        else:               # Иначе последняя цифра числа нечетная
            not_even += 1   # увеличиваем счетчик нечетных цифр not_even.
    return f'even numbers {even} | odd numbers {not_even} '

print(natur_num('34560'))

# 2ой вариант решения:
def even_odd(num: int):
    even = []
    odd = []
    while num > 0:
        n = num % 10
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
        num = num // 10
    return f'количество четных чисел {len(even)} это {even}, количество не четных чисел {len(odd)} это {odd}'
print(even_odd(34560))

