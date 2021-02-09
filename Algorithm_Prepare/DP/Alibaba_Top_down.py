import sys
sys.stdin = open('input.txt','rt')


def DFS(i,j):
    # memoization 한 데이터 값들을 이용한 Cut Edge.
    if dynamic_board[i][j] > 0:
        return dynamic_board[i][j]
    if i == 0 and j == 0:
        return board[i][j]
    elif i == 0 and j != 0:
        dynamic_board[i][j] = DFS(i,j-1) + board[i][j]
        return dynamic_board[i][j]
    elif i != 0 and j == 0:
        dynamic_board[i][j] = DFS(i-1,j) + board[i][j]
        return dynamic_board[i][j]
    else:
        dynamic_board[i][j] = min(DFS(i-1,j), DFS(i,j-1)) + board[i][j]
        return dynamic_board[i][j]


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    dynamic_board = [[0]*N for _ in range(N)]
    print(DFS(N-1,N-1))