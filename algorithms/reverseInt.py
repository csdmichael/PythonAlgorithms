class Solution:
    def reverse(self, x: int) -> int:
        unsignedX = x
        isPostive = True
        if (unsignedX < 0):
            unsignedX *= -1
            isPostive = False
        s = str(unsignedX)
        s = s[::-1]
        res = int(s)
        if (res > 2**31 - 1):
            res = 0
        if not isPostive:
            res *= -1
        return res

#print(2**31)
y = Solution.reverse(Solution, 1534236469)
print(y)