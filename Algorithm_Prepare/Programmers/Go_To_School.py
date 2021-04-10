def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]

    # 1. make puddle and fisrst setting
    board[0][0] = 1  # start point = 1
    for puddle in puddles:
        board[puddle[0] - 1][puddle[1] - 1] = -1

    for i in range(n):
        for j in range(m):
            if i == 0 and j > 0 and board[i][j] != -1:
                if board[i][j - 1] != -1:
                    board[i][j] += board[i][j - 1]
            elif i > 0 and j > 0 and board[i][j] != -1:
                if board[i][j - 1] != -1:
                    board[i][j] += board[i][j - 1]
                if board[i - 1][j] != -1:
                    board[i][j] += board[i - 1][j]
            elif i > 0 and j == 0 and board[i][j] != -1:
                if board[i - 1][j] != -1:
                    board[i][j] += board[i - 1][j]
            if board[i][j] != -1:
                board[i][j] %= 1000000007

    return board[n - 1][m - 1]


if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2,2]]
    print(solution(m, n, puddles))