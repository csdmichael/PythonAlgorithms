from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        maxA = 0
        l = 0
        r = len(height) - 1
        while (r > l):
            x = r - l
            if (height[l] < height[r]):
                y = height[l]
                l += 1
            else:
                y = height[r]
                r -= 1
            area = x * y
            if area > maxA:
                maxA = area

        return maxA

i = [1,8,6,2,5,4,8,3,7]
y = Solution.maxArea(Solution, i)
print(y)