class Solution:
    def getFirstNonRepeatedCharacter(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in s:
            if char_count[char] == 1:
                return char
        return ''
    
# Example usage:
solution = Solution()
print(solution.getFirstNonRepeatedCharacter("swiss"))  # Output: "w"