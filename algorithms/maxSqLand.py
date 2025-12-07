def findMaxSquareLand(land):
    if not land or not land[0]:
        return 0

    rows = len(land)
    cols = len(land[0])
    max_side = 0

    # Create a DP table to store the size of the largest square ending at (i, j)
    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 1:  # Land cell
                if i == 0 or j == 0:
                    dp[i][j] = 1  # First row or first column
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side  # Return the area of the largest square