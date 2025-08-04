from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = 0.0
        merged = nums1 + nums2
        print(merged)
        l = len(merged)
        sum = 0
        for i in range(l):
            sum += merged[i]
        res = sum / l
        return res
    
y = Solution.findMedianSortedArrays(Solution, [1,2], [3,4])
print(f"Result: {y}")
