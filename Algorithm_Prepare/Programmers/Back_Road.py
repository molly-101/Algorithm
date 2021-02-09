def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    dynamic_board = [[0] * m for _ in range(n)]
    for puddle in puddles:
        board[puddle[1] - 1][puddle[0] - 1] = 1

    dynamic_board[0][0] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] != 1:
                # upside
                if i == 0 and j == 0:
                    continue
                if i == 0 and j != 0:
                    dynamic_board[i][j] = dynamic_board[i][j - 1]
                    continue
                if j == 0 and i != 0:
                    dynamic_board[i][j] = dynamic_board[i - 1][j]
                    continue
                dynamic_board[i][j] = dynamic_board[i - 1][j] + dynamic_board[i][j - 1]
            else:
                dynamic_board[i][j] = 0
    print(dynamic_board)
    return dynamic_board[n - 1][m - 1] % 1000000007


if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2,2]]
    print(solution(m,n,puddles))