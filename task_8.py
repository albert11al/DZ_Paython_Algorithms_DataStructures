# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def how_many_numbers(num: int, what_num: int):
    count = 0
    for i in range(1, num + 1):
        nums = int(input("Число " + str(i) + ": "))
        while nums > 0:
            if nums % 10 == what_num:
                count += 1
            nums = nums // 10
    return f'Было введено {count} цифр {what_num}'

num = int(input("Сколько будет чисел? "))
what_num = int(input("Какую цифру считать? "))
print(how_many_numbers(num, what_num))
