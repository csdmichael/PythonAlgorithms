from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        ctr = 0
        ptr = 0
        while ptr < len(nums):
            curr = nums[ptr]
            if curr == prev:
                if ctr == 2:
                    nums.remove(curr)
                    ptr -= 1
                else:    
                    ctr += 1
            else:
                ctr = 1
                prev = curr
            ptr += 1
        return nums
    
x = [1,1,1,2,2,3]#[0,0,1,1,1,1,2,3,3]
y = Solution.removeDuplicates(Solution, x)
print(y)
