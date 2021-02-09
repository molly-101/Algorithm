import sys
sys.stdin = open('input.txt', 'rt')


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    memo = [[0]*(N) for _ in range(N)]
    memo[0][0] = board[0][0]

    for i in range(N):
        for j in range(N):
            if i == 0 and j != 0:
                    memo[i][j] = board[i][j] + memo[i][j-1]
                    continue
            if j == 0 and j != 0:
                    memo[i][j] = board[i][j] + memo[i-1][j]
                    continue
            if memo[i][j-1] > memo[i-1][j]:
                memo[i][j] = board[i][j] + memo[i-1][j]
            else:
                memo[i][j] = board[i][j] + memo[i][j-1]
    print(memo[N-1][N-1])