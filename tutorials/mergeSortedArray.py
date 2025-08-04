class MergeSortedArray:
    def merge(nums1: list[int], nums2: list[int]) -> list[int]:
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        merged = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < n:
            merged.append(nums1[i])
            i += 1
        while j < m:
            merged.append(nums2[j])
            j += 1
        return merged

print("Started")         
a = MergeSortedArray
nums1 = [1,2,3]
nums2 = [2,5,6]
merged = a.merge(nums1, nums2)
print(merged)

nums1 = [1]
nums2 = []
merged = a.merge(nums1, nums2)
print(merged)

nums1 = []
nums2 = [2]
merged = a.merge(nums1, nums2)
print(merged)