class TrieNode:
    def __init__(self):
        self.links = dict()
        self.is_world = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if node.links.get(char) is None:
                node.links[char] = TrieNode()
            node = node.links[char]
        node.is_world = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.is_world:
                self.res = True
            return
        if word[0] == '.':
            for child in node.links.values():
                self.dfs(child, word[1:])
        else:
            node = node.links.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])

'''разбор решения'''
class TrieNode:
    def __init__(self):
        self.links = dict()
        self.is_world = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root# достаем корень
        for char in word:#пробегаемся по каждому синволу в слове, которое нужно вставить
            if node.children.get(char) is None:# если не такого синвола в дере
                node.links[char] = TrieNode()# то мы ее добовляем
            node = node.links[char]# и спускаемся дальше
        node.is_world = True# и помечаем этот узел уже словом

    def search(self, word):#поиск слова
        node = self.root# начинаем поиск слова с корня
        self.res = False # заводим флажок с результатом
        self.dfs(node, word)# рекурсивная функция для поиска слова со всеми точками.
            # будем передовать node и место с ним в нашу функцию будем передовать слово word которое надо найти
        return self.res # и будем возврашать нсобранный результат

    def dfs(self, node, word):# изначально передаем узел и слово которое нужно нойти
        # проверяем если в функцию dfs приходит пустое слово в word то будем проверять node которым мы находимся является словом
        if not word:# если не слово то делаем дополнительно проверку
            if node.is_world: # если слово то в результат записываем
                self.res = True #то в результат записываем True
            return   #если строка пустая выходим из функции
        if word[0] == '.':# если слово которое пришло и ее первый элемент равен точке(.)
            for child in node.links.values():# для каждого ноде из словаря достаем их значения(values). ключ это синво, а ноде это значение
                self.dfs(child, word[1:]) # запускаем поиска. передаем срез с 1-го синвола
        else:# если не точка
            node = node.links.get(word[0])# то берем ноду от 1-го синвола, чтобы спустица ниже
            if not node: #проверим если нода
                return # если ноды нет выходим из функции
            self.dfs(node, word[1:])#еслс есть запускаем функции от этой же ноды и тоже передаем её срез слова

