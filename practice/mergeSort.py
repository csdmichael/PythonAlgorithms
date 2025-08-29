from math import floor
from typing import List
class Solution:
    def mergeSort(self, arr: List[int]) -> List[int]:
        return self.__divideAndConquer(self, arr, 0, len(arr) - 1)
    
    def __divideAndConquer(self, arr: List[int], start: int, end: int) -> List[int]:
        if end == start:
            return arr[start:end + 1]
        else:
            mid = start + floor((end - start) / 2)
            left = self.__divideAndConquer(self, arr, start, mid)
            right = self.__divideAndConquer(self, arr, mid + 1, end)
            res = self.__merge(self, left, right)
            return res
        
    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        l = 0
        r = 0
        merged = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        if l < len(left):
            merged += left[l: len(left)]
        if r < len(right):
            merged += right[r: len(right)]
        
        return merged

y = Solution.mergeSort(Solution, [7,3,5,2,8,1,9])
print(y)