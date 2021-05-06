from collections import deque


def solution(board):
    # initialize memo -> save minimum money to build race track
    memo = [[float('inf')]*len(board) for _ in range(len(board))]
    memo[0][0] = 0

    # initialize start deque, dx, dy
    # note : up = 0, right = 1, down = 2, left = 3
    dq = deque([[0, 0, 2, 0], [0, 0, 1, 0]])
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    while dq:
        now = dq.popleft()
        for i in range(4):
            tmpx, tmpy = now[0] + dx[i], now[1] + dy[i]

            if 0 <= tmpx < len(board) and 0 <= tmpy < len(board) and board[tmpx][tmpy] != 1:
                # maintain line
                if abs(i - now[2]) == 0 and now[3] + 100 <= memo[tmpx][tmpy]:
                    memo[tmpx][tmpy] = now[3] + 100
                    dq.append([tmpx, tmpy, i, now[3]+100])
                # vertical move
                elif abs(i - now[2]) % 2 == 1 and now[3] + 600 <= memo[tmpx][tmpy]:
                    memo[tmpx][tmpy] = now[3] + 600
                    dq.append([tmpx, tmpy, i, now[3]+600])

    return memo[len(memo)-1][len(memo)-1]


if __name__ == "__main__":
    board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]]
    print(solution(board))