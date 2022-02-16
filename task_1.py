# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# вход: целое число
# выход: сумма и произведение цифр целого числа
def sum_num_bad(num: int) -> int:
    mult = 1
    sum = 0
    while (num != 0):
        mult = mult * (num % 10)
        sum = sum + num % 10
        num = num // 10
    print("Произведение цифр равно: ", mult)
    print("Сумма цифр числа равна: ", sum)
sum_num_bad(256)

# вариант решения
#num = int(input("Введите целое: "))
#a = list(map(int, str(num)))
#print(f' sum {a[0]+a[1]+a[2]} mult {a[0]*a[1]*a[2]}')

