class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        chars = {}
        l = len(s)
        for i in range(l):
            currChar = s[i]
            if currChar in chars:
                
                left = chars[currChar][len(chars[currChar]) - 1]
                               
                print(chars)
                print(f"{currChar}: Left: {left}")
                print(f"Max Length: {maxLength}")
                print("-------------------")
                chars[currChar].append(i)
            else:
                chars[currChar] = [i]
                if (i - left + 1) > maxLength:
                    maxLength = i - left + 1
        return maxLength

s = "abcabcbb"
#s = " "
y = Solution.lengthOfLongestSubstring(Solution, s)
print(y)