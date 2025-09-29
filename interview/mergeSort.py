import math

class Solution:
    def mergeSort(self, arr: list) -> list:
        start = 0
        end = len(arr) - 1
        return self.__partitionAndMerge(self, arr, start, end)
    
    def __partitionAndMerge(self, arr: list, start: int, end: int) -> list:
        if (end == start):
            return arr[start : end+1]
        else:
            mid = start + math.floor((end - start) / 2)
            left = self.__partitionAndMerge(self, arr, start, mid)
            right = self.__partitionAndMerge(self, arr, mid + 1, end)
            return self.__merge(left, right)
    
    def __merge(left: list, right: list) -> list:
        merged_list: list = []
        l = 0
        r = 0
        m = 0
        lenLeft = len(left)
        lenRight = len(right)
        while l < lenLeft and r < lenRight:
            if (left[l] < right[r]):
                merged_list.append(left[l])
                l += 1
            else:
                merged_list.append(right[r])
                r += 1

        while l < lenLeft:
            merged_list.append(left[l])
            l += 1
        
        while r < lenRight:
            merged_list.append(right[r])
            r += 1

        return merged_list

s = Solution
y = s.mergeSort(s, [5,2,8, 1, 4, 3])
print(y)