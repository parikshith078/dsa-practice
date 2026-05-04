class Node:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.childrens:
                curr = curr.childrens[char]
            else:
                newNode = Node()
                curr.childrens[char] = newNode
                curr = newNode
        curr.isWord = True
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.childrens:
                return False
            else:
                curr = curr.childrens[char]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.childrens:
                return False
            else:
                curr = curr.childrens[char]
        return True
        
        