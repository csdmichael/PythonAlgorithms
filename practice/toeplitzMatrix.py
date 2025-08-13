from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[int][int]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if rows < 2 or cols < 2:
            return True
        #Horizontal Scan for diameters
        for c in range(cols - 2):
            i,j = 0,c
            curr = matrix[i][j]
            while j < cols - 1 and i < rows - 1:
                if matrix[i][j] != curr:
                    return False
        #Vertical Scan for diameters
        for r in range(rows - 2):
            i,j = r,0
            curr = matrix[i][j]
            while j < cols - 1 and i < rows - 1:
                if matrix[i][j] != curr:
                    return False
        return True
    
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]