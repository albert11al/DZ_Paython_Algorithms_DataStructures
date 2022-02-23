# 1/dop. Не выделяйте дополнительное пространство для другого массива,
# вы должны сделать это, изменив входной массив на месте с помощью дополнительной памяти O (1)..
#Пример:
#Ввод: s = ["H","a","n","n","a","h"]
#Вывод: ["h","a","n","n","a","H"]
def print_revers_recur(s: list[str]):
    def helper(str, i):
        if i >= len(str):
            return
        helper(str, i+1)
        print(s[i], end=' ')
    helper(s, 0)

s = ["h","e","l","l","o"]
print_revers_recur(s)

# 2ой вариант решения (решения которое показал преподователь, не понемаю как работает код)
def rev(arr, i=0):
    if i >= len(arr) // 2:
        return
    arr[i], arr[-(i + 1)] = arr[-(i + 1)], arr[i]
    rev(arr, i + 1)

test = ["t", "e", "s", "t"]
print(rev(test))

