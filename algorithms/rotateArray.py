from typing import List
class Solution:
    def rotateArrayInPlace(nums:List[int], k: int)->None:
        right = len(nums) - 1
        left = k - 1
        for i in range(k):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            right -= 1
            left -= 1
        print(nums)

nums = [1,2,3,4,5,6,7]
k = 3

Solution.rotateArray(nums, k)
