class Solution:
    def areAlmostEqual(self, firstWord: str, secondWord: str) -> bool:
        if firstWord == None or secondWord == None:
            return False
        if len(firstWord) != len(secondWord):
            return False
        firstWord = firstWord.lower()
        secondWord = secondWord.lower()

        hashMap = {}
        for c in firstWord:
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c] = 1
        
        for c in secondWord:
            if c in hashMap:
                hashMap[c] -= 1
                if hashMap[c] == 0:
                    del hashMap[c]
            else:
                return False
            
        if len(hashMap) == 0:
            return True
        return False       

y = Solution().areAlmostEqual("Bank", "Kanb")
print(y)