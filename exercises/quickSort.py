def quickSort(arr: list[int])->list[int]:
    if len(arr) <= 1:
        return arr
    # Assume pivot as 1st element
    pivot = arr[0]
    left = []
    right = []
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = quickSort(left)
    right = quickSort(right)
    return left + [pivot] + right

y = quickSort([8,5,3,7,5,2,1])
print(y)