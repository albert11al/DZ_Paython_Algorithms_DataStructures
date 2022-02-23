# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def foo(num: int):
    sum_num = 0
    result = n*(n+1)//2
    for i in range(1, num + 1):
        sum_num += i
        if sum_num == result:
            print('равенство выполняется')
    return f' 1+2+...+n = {sum_num} | n(n+1)/2 = {result}'

n = int(input('введите натуральное чисдо: '))
print(foo(n))
