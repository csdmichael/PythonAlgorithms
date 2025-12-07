class TrieNode:
    def __init__(self):
        # Use a dictionary to store children nodes, where keys are characters
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time complexity: O(L), where L is the length of the word.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # Mark the end of the word after all characters are added
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Checks if a word exists in the trie.
        Time complexity: O(L), where L is the length of the word.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # A word is found only if the last node is marked as the end of a word
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if there is any word in the trie that starts with the given prefix.
        Time complexity: O(L), where L is the length of the prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # If we reach the end of the prefix, it means a path exists
        return True