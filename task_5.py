# Учитывая целочисленный массив nums, переместите все 0 в его конец,
# сохраняя относительный порядок ненулевых элементов.

# Обратите внимание, что вы должны сделать это на месте, не создавая копию массива.

#например
#Ввод: числа = [0,1,0,3,12]
#Вывод: [1,3,12,0,0]
import unittest
def move_zeros(array):
    i = 0
    limit = len(array)
    while i < limit:
        if array[i] == 0:
            for j in range(i, limit - 1):
                array[j] = array[j + 1]
            array[limit - 1] = 0
            limit -= 1
        else:
            i += 1
    print(array)
    return array
class TestMoveZeros(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual([1, 3, 5, 12, 4, 0, 0], move_zeros([0,1,0,3,5,12,4]))
        self.assertEqual([1,3,12,0,0], move_zeros([0,1,0,3,12]))
        self.assertEqual([0,0,0,0], move_zeros([0,0,0,0]))
        self.assertEqual([1, 1, 3, 12], move_zeros([1, 1, 3, 12]))
        self.assertEqual([5,0,0,0,0], move_zeros([0,0,0,0,5]))
