#Учитывая целочисленный массив nums, вернуть true, если какое-либо значение встречается
#в массиве хотя бы дважды, и вернуть false, если все элементы различны.
#Ввод: числа = [1,2,3,1]
#Вывод: правда
#Ввод: числа = [1,2,3,4]
#Вывод: ложь
#Ввод: числа = [1,1,1,3,3,4,3,2,4,2]
#Вывод: правда

class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                return True
        return False
#--------------------------------------------------------
# варианты решения
num1 = [1,1,1,3,3,4,3,2,4,2]
num2 = [1,2,3,4]
num3 = [1,2,3,1]
#отсортируем значения, если встречаются два последовательно одинаковые числа тогда true и если не совподает дойдет до конца и вернет false
#например: [1,2,3,1] -> sorted ['1,1',2,3] true
def b_nums(nums: list):
    nums = sorted(nums)
    for i in range(len(nums)-1): #-1 это индекс. значит повторение до конца
        if nums[i] == nums[i+1]: # если значения по индексу nums[i] равно следубшему значению nums[i+1] тогда возврашает true
            return True          # и если дойдёт до конца и не найдет равенство значит false
    return False
print(b_nums(num1))
print(b_nums(num2))
print(b_nums(num3))
print('------------------------------------------')
#----------------------------------------------------------------
def a_nums(nums: list):
    return len(nums) != len(set(nums))
print(a_nums(num1))
print(a_nums(num2))
print(a_nums(num3))
print('------------------------------------------')
#----------------------------------------------------------------
def d_nums(nums: list):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
print(d_nums(num1))
print(d_nums(num2))
print(d_nums(num3))
