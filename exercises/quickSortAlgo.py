def sort(arr: list[int]) -> list[int]:
    
    if len(arr) <= 1:
        return arr
    pivotIndex = 0 #To do: Enhance pivot selection - e.g. Random pivot
    pivot = arr[pivotIndex]

    left = []
    right = []

    # Elements smaller than pivot go to left sub array
    # Else they go to right sub array
    for i in range(len(arr)):
        if i != pivotIndex:
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
    
    # Repeat for left, right sub arrays
    left = sort(left)
    right = sort(right)

    return left + [pivot] + right


y = sort([5,3,8,1,4,2])
print(y)