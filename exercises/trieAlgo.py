class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word: bool

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def searchWord(self, word: str)->bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str)->bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True