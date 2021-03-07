import sys
from collections import deque
sys.stdin = open('input.txt','rt')


def solution(N, M, board, start_r, start_c, passenger, fuel):
    # make board in passenger
    psg_dic = {}
    for i in range(len(passenger)):
        board[passenger[i][0]-1][passenger[i][1]-1] = i+100
        psg_dic[i+100] = [passenger[i][2]-1, passenger[i][3]-1]

    dQ = deque()
    dQ.append([start_r-1, start_c-1])

    memo = [[0]*N for _ in range(N)]
    memo[start_r-1][start_c-1] = 1

    dx, dy = [-1,0,1,0], [0,1,0,-1]
    state = 0
    fuel_add = 0
    finish = []
    arrived = 0

    while dQ:
        if state == 0:
            ride = []
            fuel -= 1

            if board[dQ[0][0]][dQ[0][1]] > 99:
                ride.append([dQ[0][0], dQ[0][1]])
                continue

            if fuel < 0:
                return -1

            for _ in range(len(dQ)):
                start = dQ.popleft()

                for i in range(4):
                    tmpx, tmpy = start[0]+dx[i], start[1]+dy[i]

                    if 0 <= tmpx < N and 0 <= tmpy < N and board[tmpx][tmpy] != 1 and memo[tmpx][tmpy] != 1:
                        if board[tmpx][tmpy] > 99:
                            ride.append([tmpx,tmpy])
                            memo[tmpx][tmpy] = 1
                        else:
                            dQ.append([tmpx,tmpy])
                            memo[tmpx][tmpy] = 1
            if ride:
                pick = sorted(ride, key= lambda x: (x[0], x[1]))[0]
                state = 1
                dQ.clear()
                dQ.append(pick)
                finish.append(psg_dic[board[pick[0]][pick[1]]])
                memo = [[0]*N for _ in range(N)]
                memo[pick[0]][pick[1]] = 1
                board[pick[0]][pick[1]] = 0

        else:
            fuel -= 1
            fuel_add += 1

            if fuel < 0:
                return -1

            for _ in range(len(dQ)):
                start = dQ.popleft()

                for i in range(4):
                    tmpx, tmpy = start[0]+dx[i], start[1]+dy[i]

                    if 0 <= tmpx < N and 0 <= tmpy < N and memo[tmpx][tmpy] != 1:
                        if finish[0] == [tmpx, tmpy]:
                            finish.pop()
                            fuel += (fuel_add * 2)
                            dQ.clear()
                            dQ.append([tmpx,tmpy])
                            state = 0
                            memo = [[0]*N for _ in range(N)]
                            memo[tmpx][tmpy] = 1
                            arrived += 1
                            fuel_add = 0
                            break

                        else:
                            dQ.append([tmpx,tmpy])
                            memo[tmpx][tmpy] = 1

                if state == 0:
                    break

        if arrived == M:
            return fuel

    return -1


if __name__ == "__main__":
    N, M, fuel = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(N)]

    start_r, start_c = map(int,input().split())

    passenger = [list(map(int,input().split())) for _ in range(M)]

    print(solution(N, M, board, start_r, start_c, passenger, fuel))
