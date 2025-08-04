class Solution:
    def longestPalindrome(s: str) -> str:
        res = ""
        resLen = 0
        if s == None or len(s) == 0:
            return res
        if s == 1:
            res = s
            resLen = 1
            return res
        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1

            #Even Length
            l, r = i, i + 1
            while l >= 0 and r < l and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
        print("Max Length", resLen)
        return res
    
res = Solution.longestPalindrome("abbazzddaddzz4df")
print("Longest Plalindrome", res)