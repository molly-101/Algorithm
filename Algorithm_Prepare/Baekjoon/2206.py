import sys
sys.stdin = open('input.txt','rt')
from collections import deque


def solution(n, m, board):
    # 1. make player use deque
    dQ = deque()
    dQ.append([[0, 0], True]) # [위치, 벽뚫가능]

    # 2. make check board when player already gone
    check_break_board, check_board = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
    check_break_board[0][0], check_board[0][0] = 1, 1

    # 3. before travel board make decision dx, dy and return value "answer"
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    answer = -1
    cnt = 1

    if n == 1 and m == 1:
        return 1
    while dQ:
        for _ in range(len(dQ)):
            cur = dQ.popleft()
            for i in range(4):
                tmpx, tmpy = cur[0][0]+dx[i], cur[0][1]+dy[i]
                if 0 <= tmpx < n and 0 <= tmpy < m:
                    if board[tmpx][tmpy] == 1 and cur[1] and check_break_board[tmpx][tmpy] == 0:
                        check_break_board[tmpx][tmpy] = 1
                        dQ.append([[tmpx, tmpy], False])
                    elif board[tmpx][tmpy] == 0 and cur[1] and check_board[tmpx][tmpy] == 0:
                        check_board[tmpx][tmpy] = 1
                        dQ.append([[tmpx,tmpy], cur[1]])
                    elif board[tmpx][tmpy] == 0 and not cur[1] and check_break_board[tmpx][tmpy] == 0:
                        check_break_board[tmpx][tmpy] = 1
                        dQ.append([[tmpx,tmpy], cur[1]])
        cnt += 1

        if check_board[n-1][m-1] == 1 or check_break_board[n-1][m-1] == 1:
            answer = cnt
            break

    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, list(input()))))
    print(solution(n, m, board))