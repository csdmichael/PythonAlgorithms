from typing import List
from math import floor

class Solution:
    def binarySearch(self, nums: List[int], x: int) -> int:
        if nums == None:
            return - 1
        res = self.findElement(nums, x, 0, len(nums) - 1)
        return res
    
    def findElement(self, nums: List[int], x: int, start: int, end: int):
        #print(start, end)
        if end == start:
            if x == nums[start]:
                return start
            else:
                return - 1
        else:
            mid = start + floor((end - start) / 2)
            if x == nums[mid]:
                return mid
            else:
                if x < nums[mid]:
                    return self.findElement(nums, x, start, mid)
                else:
                    return self.findElement(nums, x, mid + 1, end)
                
s = Solution()
res = s.binarySearch([1,2,4,5,6], 3)
print(res)