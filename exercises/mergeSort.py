from math import floor

def mergeSort(arr: list[int])->list[int]:
    if arr == None:
        return arr
    start = 0
    end = len(arr)
    return partition_merge(arr, start, end)

def partition_merge(arr: list[int], start, end)-> list[int]:
    if end == start:
        return arr[start : end + 1]
    else:
        mid = start + floor((end - start) / 2)
        left = partition_merge(arr, start, mid)
        right = partition_merge(arr, mid + 1, end)
        res = merge(left, right)
        return res
    
def merge(left: list[int], right: list[int])->list[int]:
    merged = []
    leftLen = len(left)
    rightLen = len(right)
    pLeft = 0
    pRight = 0

    while pLeft < leftLen and pRight < rightLen:
        if left[pLeft] < right[pRight]:
            merged.append(left[pLeft])
            pLeft += 1
        else:
            merged.append(right[pRight])
            pRight += 1

    if pLeft < leftLen:
        merged += left[pLeft: leftLen]

    if pRight < rightLen:
        merged += right[pRight: rightLen]

    return merged

        
    