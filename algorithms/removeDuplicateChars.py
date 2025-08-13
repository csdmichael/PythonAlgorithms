class Solution:
    def removeAdjDuplicateChars(s: str) -> str:
        res = ""
        for char in s:
            if len(res) == 0:
                res += char
            else:
                l = len(res)
                if char != res[l - 1]:
                    res += char
        return res
    
    def removeAllDuplicateChars(s: str) -> str:
        res = ""
        hash = {}
        for char in s:
            if len(res) == 0:
                res += char
                hash[char] = 1
            else:
                l = len(res)
                if char not in hash:
                    res += char
                    hash[char] = 1
        return res
x = "abddcccW"
x = "ceerfgegfreggdsve"

y = Solution.removeAdjDuplicateChars(x)
print("Remove Adj result:", y)
y = Solution.removeAllDuplicateChars(x)
print("Remove all result:", y)