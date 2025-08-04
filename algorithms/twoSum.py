class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res = []
        visited = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in visited:
                res.append(visited[diff])
                res.append(i)
                break
            else:
                visited[curr] = i
        return res

#y = Solution.twoSum(Solution, [2,7,11,15], 9)

y = Solution.twoSum(Solution, [3,2,4], 6)
print(y)