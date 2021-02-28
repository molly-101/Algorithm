import sys
from collections import deque
sys.stdin = open('input.txt','rt')


def minMovs(n, m, board, x,y):  # n: 행, m: 열, board: 판, x,y: F 좌표
    # 1. 코인 개수 카운트 -> 리스트 크기 조절하기 위해, 각 위치마다 좌표 저장
    cur_list = [[0,0]]  # 좌표를 담은 리스트 dis_list 와 동일한 인덱스 start 는 먼저 넣어준다.
    coin_cnt = 0   # coin counter
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                coin_cnt += 1
                cur_list.append([i,j])
                board[i][j] = 10 + coin_cnt  # 벽과 코인 번호를 구분하기 위해서

    cur_list.append([x, y])  # F 좌표도 결국 도착지점이므로 저장해준다.

    # 2. 모든 거리를 담을 리스트 생성해줍니다 (start, coin, F)
    dis_list = []  # 0번에는 start, end 에는 F, coin 들은 각자 번호별로 매칭되는 리스트
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    board[x][y] = 11 + coin_cnt  # F 도 10+index 로 만들어 주어야 코인으로 인식한다.
    board[0][0] = 10             # start 도 10+index 로 만들어 주어야 코인으로 인식한다.

    for i in range(len(cur_list)):
        Q = deque()
        Q.append(cur_list[i])
        distance_cnt = 0  # 기준이 되는 곳으로 부터 떨어진 거리를 저장
        tmp_board = [[0]*m for _ in range(n)]  # 시작점부터 지나온 위치들을 저장해주는 board 와 동일한 크기의 리스트
        tmp_board[cur_list[i][0]][cur_list[i][1]] = 1  # 시작하는 곳에 다시 오면 안되므로 미리 지나갔다고 표시해준다.
        while Q:
            distance_cnt += 1
            for _ in range(len(Q)):
                cur = Q.popleft()  # 현재 위치 커서
                for k in range(4):
                    tmp_x, tmp_y = cur[0]+dx[k], cur[1]+dy[k]
                    # 공간을 벗어나지 않으면서 board 값이 10 보다 크고(start 부터 coin 들을 지나 F 까지 10을 더했으므로)이전에 지나온 적이 없는 길
                    if 0 <= tmp_x < n and 0 <= tmp_y < m and board[tmp_x][tmp_y] != 1:
                        if tmp_board[tmp_x][tmp_y] == 0:
                            if board[tmp_x][tmp_y] >= 10:  # start or coins or end point
                                tmp_board[tmp_x][tmp_y] = 1
                                dis_list.append([i,board[tmp_x][tmp_y]-10,distance_cnt])
                                Q.append([tmp_x, tmp_y])
                            else:  # board 에 1 즉, 벽인 부분
                                tmp_board[tmp_x][tmp_y] = 1
                                Q.append([tmp_x, tmp_y])


# 3. Disjoint set (Union-Find) 알고리즘, 크루스칼 알괴즘으로 Cycle 이 생기지 않으며 최저 비용으로 이을 수 있는 가지만 남기기
def disjoint_set(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connection = [costs[0][0]]
    while len(connection) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connection) and (cost[1] in connection):
                continue
            if (cost[0] in connection) or (cost[1] in connection):
                answer += cost[2]
                connection.append(cost[0])
                connection.append(cost[1])
                print(cost[0],cost[1])
                connection = list(set(connection))
                costs.pop(i)
                print(answer)
                break
    return answer




if __name__ == "__main__":
    n = int(input())
    m = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    x = int(input())
    y = int(input())
    minMovs(n, m, board, x, y)