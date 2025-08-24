from typing import List
import heapq

class Solution:
    def fifthLargest(self, arr: List[int]):
        # code here
        if len(arr) < 5:
            return -1
        maxHeap = []
        for i in arr:
            heapq.heappush(maxHeap, -i)
        return maxHeap[4] * -1
        
        
y = Solution.fifthLargest(Solution, [2, 4, 3, 5, 6, 8, 7])
print(y)