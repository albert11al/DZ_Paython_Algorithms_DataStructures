import unittest
def delete_copyy(app: list) -> list:
    ints_list = app
    ints_list = list(set(ints_list))
    print(ints_list)
    return ints_list

class TestDeleteCopy(unittest.TestCase):
    def test_delete(self):
        self.assertEqual([2, 3, 4, 5, 6], delete_copyy([2, 3, 3, 2, 5, 4, 4, 6]))
        self.assertEqual([2], delete_copyy([2, 2, 2, 2, 2]))
        self.assertEqual([2, 3, 5], delete_copyy([2, 3, 3, 2, 5]))
        self.assertEqual([2, 3, 5, 7], delete_copyy([7, 3, 2, 5]))