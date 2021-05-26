def solution(triangle):
    memo = [[0] * (i + 1) for i in range(len(triangle))]
    memo[0][0] = triangle[0][0]
    result = 0

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                memo[i][j] = triangle[i][j] + memo[i - 1][j]
            elif j == len(triangle[i]) - 1:
                memo[i][j] = triangle[i][j] + memo[i - 1][j - 1]
            else:
                memo[i][j] = triangle[i][j] + max(memo[i - 1][j - 1], memo[i - 1][j])

            result = max(memo[i][j], result)

    return result
