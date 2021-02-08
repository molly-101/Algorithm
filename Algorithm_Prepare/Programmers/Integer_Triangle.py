def solution(triangle):
    memo = [[0]*(i) for i in range(1,len(triangle)+1)]
    memo[0] = triangle[0]
    maximum = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                memo[i][j] = memo[i-1][j] + triangle[i][j]
                if maximum < memo[i][j]: maximum = memo[i][j]
            elif j == len(triangle[i])-1:
                memo[i][j] = memo[i-1][j-1] + triangle[i][j]
                if maximum < memo[i][j]: maximum = memo[i][j]
            else:
                if memo[i-1][j-1] < memo[i-1][j]:
                    memo[i][j] = memo[i-1][j] + triangle[i][j]
                else:
                    memo[i][j] = memo[i-1][j-1] + triangle[i][j]
                if maximum < memo[i][j]: maximum = memo[i][j]
    return maximum



if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    solution(triangle)