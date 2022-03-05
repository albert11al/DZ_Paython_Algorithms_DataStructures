#145/1.Учитывая корень бинарного дерева, верните обход значений его узлов в обратном порядке.
#Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень:

class Solution(object):
    def postorderTraversal(self, root):
        if root is None: # если корень пришел нулевой то мы вернем пустой массив, а дальше
            return[]
        stack = [root] # в stack кладём корень
        res = [] # масив куда складывается результат
        while stack: # пока в stack есть элементы
            node = stack.pop() # достаем из stack элемент с права
            res.append(node.val) # т.к. сначала посешаем корень в ответ записываем текушую node и проверим.
            if node.left != None: # если у нас есть левый элемент то мы бросаем его в stack
                stack.append(node.left)
            if node.right != None:# если у нас есть правый элемент то мы бросаем его в stack
                stack.append(node.right)
        return res[::-1]

#----------------------------------------------------------------------------------------------------------
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def hellper(node):
            if node.left:               # сначала посешаем лево
                hellper(node.left)
            if node.right:              # потом посешаем право
                hellper(node.right)
            res.append(node.val) #все рекурсивные функции закончились добовляем в ответ кореньт.е. node который приходит на вход функции

        if root is None:
            return res

        hellper(root)
        return res