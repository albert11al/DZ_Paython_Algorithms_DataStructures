#101/ Учитывая корень бинарного дерева, проверьте, является ли он зеркалом самого себя
# (т. Е. Симметричным относительно своего центра).
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMiroor(root, root)
    def isMiroor(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.isMiroor(left.left, right.right) \
                   and self.isMiroor(left.right, right.left)

#        if root is None: # если корень равень нулю то верни истина, это значит симетрична одно значение
#           return True
#        return self.isMiroor(root, root) # иначе возврашаем рекурсивную функцию в переменные передаем значения root, чтобы проверить являются ли ее дети симетричными
#    def isMiroor(self, left, right): # функция проверяет симетрична ли соотношения root.left == root.right
#        if left == None and right == None: #если у родителя левый узел = None и правый узел точно так же = None, то это знаачит семетрия возврашаем правду
#            return True # то возврашаем истина
#        elif left == None or right == None: # иначи если  один из узло не = None, то это не симетрия и возврашаем ложь
#            return False
# если мы пройдем первые два условия это значит, что у детей, правя и левая нода сушествует, то тогда  возврашаем
#        else:
#            return left.val == right.val and self.isMiroor(left.left, right.right) \
#                   and self.isMiroor(left.right, right.left)
# если это значения равны left.val == right.val то дальше проверяем два условия
#                   #если под left.val и right.val есть дети то нам нужео использовать нашу функцию

