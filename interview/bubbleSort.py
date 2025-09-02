from typing import List

def bubbleSort(arr: List[int]):
    if arr == None:
        return None
    l = len(arr)
    
    if l == 0:
        return arr
    
    for i in range(1, l - 1):
        for j in range(0, l - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

y = bubbleSort([5,3,6,1,7,4])
print(y)
