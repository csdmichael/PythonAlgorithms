class Solution:
    def reverseSentence(self, s: str) -> str:
        stk = []
        words = s.split(' ')
        '''
        for i in range(len(words), 0, -1):
            print(words[i - 1])
        '''
        for word in words:
            stk.append(word)

        res = ""
        while len(stk) > 0:
            word = stk.pop()
            if res == "":
                res = word
            else:
                res += " " + word
        return res

y = Solution().reverseSentence("Hello my friend")
print(y)