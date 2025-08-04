class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        resLen = 0

        if (len(s)) < 1:
            return res
        if (len(s)) == 1:
            resLen = 1
            return s
        
        for i in range(len(s)):
            #Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1 
            #Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1 
                
        print(f"Max Lengtth = {resLen}")
        return res

y = Solution.longestPalindrome(Solution, "abbabad")
print(y)