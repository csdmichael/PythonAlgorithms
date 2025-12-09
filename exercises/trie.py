class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


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
    
    def starts_with(self, prefix: str)->bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
    
t = Trie()
t.addWord('Hello')
t.addWord('Helarious')
t.addWord('He')
t.addWord('Mango')

x = t.searchWord('Hello')
print(f'Hello Exists: {x}')
x = t.searchWord('Hellos')
print(f'Hellos Exists: {x}')
x = t.starts_with('Hel')
print(f'Starts with Hel: {x}')
x = t.starts_with('Ha')
print(f'Starts with Ha: {x}')