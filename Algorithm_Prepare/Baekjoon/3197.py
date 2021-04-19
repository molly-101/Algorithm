import sys
from collections import deque
sys.stdin = open('input.txt','rt')


def solution(r, c, board):
    pass


if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [[] for _ in range(R)]
    swans, water = deque(), deque()

    for i in range(R):
        tmp = sys.stdin.readline()
        for j in range(len(tmp)):
            if tmp[j] == ".": # water
                board[i].append(0)
                water.append([i,j])
            elif tmp[j] == "X": # ice
                board[i].append(1)
            elif tmp[j] == "L": # swan
                board[i].append(2)
                swans.append([i,j])

    solution(R, C, board)

    for i in board:
        for j in i:
            print(j, end=" ")
        print()
