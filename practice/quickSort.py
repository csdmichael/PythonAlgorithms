from typing import List

class Solution:
    def quickSort(self, arr:List[int]):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        left = self.quickSort(self, left)
        right = self.quickSort(self, right)

        return left + [pivot] + right

y = Solution.quickSort(Solution, [7,3,5,2,8,1,9])
print(y)