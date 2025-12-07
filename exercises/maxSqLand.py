def CalculateMaxSquareLand(land: list[list[int]]) -> int:
    rows = len(land)
    cols = len(land[0])

    maxLen = 0
    dp = [[0] * cols for _ in range(rows)]

    print(f'DP init: {dp}')

    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min([
                        dp[i][j-1], 
                        dp[i-1][j], 
                        dp[i-1][j-1]
                    ]) + 1
                    maxLen = max([maxLen, dp[i][j]])
    print(f'DP final: {dp}')
    return maxLen

ans = CalculateMaxSquareLand(
    [
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1, 1]
    ]
)

print(f'Ans = {ans}')