from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int: 
        left = 0
        right = 0
        notOnePos = -1
        maxSubArrLen = 0
        for right in range(len(nums)):
            if nums[left] != 1:
                left += 1
                continue
            if nums[right] != 1:
                if notOnePos == -1:
                    notOnePos = right
                else:
                    maxSubArrLen = max(maxSubArrLen, right - left - 1)
                    left = notOnePos + 1
                    notOnePos = -1
        maxSubArrLen = max(maxSubArrLen, right - left)
        return maxSubArrLen
#input = [0,1,1,1,0,1,1,0,1]
input = [1,1,0,1]
y = Solution.longestSubarray(Solution, input)
print(y)