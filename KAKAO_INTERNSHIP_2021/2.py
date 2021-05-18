from collections import deque


def solution(places):
    # make result
    result = []
    dx, dy = [-1,0,1,0], [0,1,0,-1]

    for place in places:
        # 모든 노드 순회, state == False -> 0 , state == True -> 1
        state = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":  # BFS 순회 시작
                    dq = deque([[i,j]])
                    ext_cnt = 0
                    memo = [[0]*5 for _ in range(5)]
                    memo[i][j] = 1

                    #BFS start
                    while ext_cnt < 2:
                        for _ in range(len(dq)):
                            tmp = dq.popleft()
                            for t in range(4):
                                tmpx, tmpy = tmp[0]+dx[t], tmp[1]+dy[t]
                                if 0 <= tmpx < 5 and 0 <= tmpy < 5 and memo[tmpx][tmpy] != 1:
                                    if place[tmpx][tmpy] == "P":
                                        state = 0
                                    elif place[tmpx][tmpy] == "O":
                                        memo[tmpx][tmpy] = 1
                                        dq.append([tmpx, tmpy])
                        ext_cnt += 1
                if state == 0:
                    break
            if state == 0:
                break
        result.append(state)

    return result




if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))