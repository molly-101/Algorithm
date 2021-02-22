import sys
sys.stdin = open('input.txt','rt')
from collections import deque

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
res = [[0]*(n) for _ in range(n)]
Q = deque()
Q.append([2,2])
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result= 0
cnt = 0
while Q:
    cnt += 1
    for j in range(len(Q)):
        start = Q.popleft()
        for i in range(4):
            tmpx, tmpy = start+dx[i],start+dy[i]
            if 0<= tmpx<= n and 0<=tmpy<=n and res[tmpx][tmpy] == 0:
                Q.append([tmpx,tmpy])
                res[tmpx][tmpy] = 1
                result += board[tmpx][tmpy]