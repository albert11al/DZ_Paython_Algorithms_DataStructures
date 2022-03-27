'''№26
Учитывая целочисленный массив nums, отсортированный в неубывающем порядке,
    удалите дубликаты на месте, чтобы каждый уникальный элемент появлялся только один раз.
    Относительный порядок элементов должен быть сохранен.
Поскольку в некоторых языках невозможно изменить длину массива,
    вместо этого вы должны поместить результат в первую часть массива nums.
    Более формально, если есть k элементов после удаления дубликатов,
    то первые k элементов nums должны содержать окончательный результат. Неважно,
    что вы оставляете за первыми k элементами.
Например:
    Ввод: числа = [0,0,1,1,1,2,2,3,3,4]
    Выход: 5, числа = [0,1,2,3,4,_,_,_,_,_]'''

class Solution(object):
    def removeDuplicates(self, nums):
        left = 1
        for right in range(1, len(nums)):
            if nums[right] == nums[right - 1]:
                continue
            nums[left] = nums[right]
            left += 1

        return left

'''разбор решения'''
#решим методом 2 указателя, где left - левый указатель куда будем перемешать уникальные знаечения
# к тому же left укажит куда будем перемешать след. уникальное значение и left выдаст количество уникальных значений
# и right - правый указатель которые будет сканировать массив
#Как узнать является ли значение уникальным? при проходе по масивом каждое значение будем сравнивать с предыдущим
# и если значение равно с предыдуши то мы ее не перемешаем в левую часть и переходим дальше right + 1
# решили за время O(n) у нас два указателя и каждый указатель будет переберать массив один раз
class Solution(object):
    def removeDuplicates(self, nums):
        left = 1# инициализируем указатель и начнем с первого индекса (таким образом сравним индекс 0 и 1)
        for right in range(1, len(nums)):# правый указатель переберает каждое значение в входном массиве
            # и так же указатель устанавливаем на 1ый индекс
            if nums[right] == nums[right] and nums[right - 1] == nums[right]:#
                # если указатель на текушем значении и равно с предыдушимзначением
                continue# то пропускаем текушее значение переходим на следуюший
            nums[left] = nums[right]# иначе присваиваем левому указателю уникальное значение
            left += 1# и сдвигаем левый указатель при каждом приваении уникального значения
            #если операция не выполняется то как и всегда увеличиваем только правый указатель

        return left


