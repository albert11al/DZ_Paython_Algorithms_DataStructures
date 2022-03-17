# Для заданного бинарного дерева найдите наименьшего общего предка (LCA) двух заданных узлов в дереве.
# Согласно определению LCA в Википедии: "Наименьший общий предок определяется между двумя узлами
# p и q как наименьший узел в T, который имеет потомками p и q (где мы позволяем узлу быть потомком самого себя)".
#Вход: root(корень) = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Выход: 3
#Объяснение: LCA узлов 5 и 1 равен 3. т.к. 3->5
#                                          3->1   итого общий узел 3

#Вход: root(корень) = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#Выход: 5
#Объяснение: LCA узлов 5 и 4 равен 5, так как согласно определению LCA узел может быть потомком самого себя.
# 3->5->2->4
# 3->5          итого общий узел 5

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left

        return root

#        if not root:
 #           return root
  #      if root == p or root == q: # если текуший узел равен p или q
   #         return root # то возврашаем этот текуший узел
# До достижения базового условия переместимся влево и вправо к текущему узлу
        # и сохраним значения в левой и правой переменных соответственно.
    #    left = self.lowestCommonAncestor(root.left, p, q)
     #   right = self.lowestCommonAncestor(root.right, p, q)
 # проверяем если у левого и правого узла значения, и возвращаем то, что не пусто среди левых и правых переменных т.е. последнее поддерево.
#        if left is None:
 #          return right
#        if right is None:
 #          return left
       # return root # Если да, вернем корневое значение, то есть родительское.



