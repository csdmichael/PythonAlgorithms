from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for j in range(cols - 1):
            i = 0
            val = matrix[i][j]
            while i < rows and j < cols:
                if  val != matrix[i][j]:
                    return False
                else:
                    i += 1
                    j += 1
        
        for i in range(rows - 1):
            j = 0
            val = matrix[i][j]
            while j < cols and i < rows:
                if  val != matrix[i][j]:
                    return False
                else:
                    i += 1
                    j += 1
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix = [[1,2],[2,2]]
y = Solution.isToeplitzMatrix(Solution, matrix)
print(y)