#Pattern: Sliding Window

class Solution:
    def getlongestStringNoRepeatChars(self, s: str) -> int: 
        l = 0
        sett = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen
    
i = "abccba"
y = Solution.getlongestStringNoRepeatChars(Solution, i)
print(y)
