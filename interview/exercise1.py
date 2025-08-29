class Solution:
    def reverseString(s: str) -> str:
        return s[::-1]
    
    def has_numbers(word: str) -> bool:
        """
        Returns True if the word contains any numeric digit, False otherwise.
        """
        return any(char.isdigit() for char in word)

    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            # Reverse if word has numbers
            if self.has_numbers(words[i]):
                words[i] = words[i][::-1]
        #words = words[::-1]
        s = " ".join(words)
        return s

y = Solution.reverseWords(Solution, "Hello World 123ABC")
print(y)

#y = Solution.reverseWords("Hello World")
#print(y)

'''
Hello World
olleH dlroW
'''