class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    def missingNumber(self, nums: list[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = True
        for i in range(len(nums) + 1):
            if i not in hashMap:
                return i
        
    
# Example usage:
solution = Solution()
print(solution.missingNumber([3, 0, 1]))  # Output: 2
print(solution.missingNumber([0, 1]))  # Output: 2
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8
# The function calculates the expected sum of numbers from 0 to n and subtracts the actual sum of the given array to find the missing number.
