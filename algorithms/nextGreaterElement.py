#Pattern: Monotonic Stack

class Solution:
    def getNextGreaterElement(arr) -> list:
        n = len(arr)
        result = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                result[stack.pop()] = arr[i] 
            stack.append(i)
        return result
    
y = Solution.getNextGreaterElement([1,4,6,3,2,7])
print(y)