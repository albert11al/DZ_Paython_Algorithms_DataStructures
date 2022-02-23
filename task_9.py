# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_num_bad(num: int):
    nums = [int(input("Число " + str(i) + ": ")) for i in range(1, num+1)]
    max_sum = 0
    max_num = 0
    for i in range(len(nums)):
        nums[i] = str(nums[i])
        s = sum(list(map(int, nums[i])))
        print('натуральное число', nums[i], 'сумма цифр', s)
        if s > max_sum:
            max_sum = s
            max_num = nums[i]
    print('максимальная сумма цифр', max_sum, 'из натурального числа', max_num)

num = int(input("Сколько будет чисел? "))
sum_num_bad(num)
