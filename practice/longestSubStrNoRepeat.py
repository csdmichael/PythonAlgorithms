class Solution:
    def longestSubStrNoRepeat(self, s: str) -> int:
        l = 0
        sett = set()
        maxLen = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(l)
                l += 1
            sett.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen

