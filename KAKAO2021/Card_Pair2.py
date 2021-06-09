from collections import deque
from itertools import permutations
import copy


def solution(board, r, c):
    # board 내의 최대값 찾고 순서 리스트 생성
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    M = 0
    for i in board:
        for j in i:
            M = max(M, j)

    orders = [i for i in range(1, M + 1)]
    result = 2000

    for order in permutations(orders):
        dq = deque([[r, c]])
        cnt = 0
        nboard = copy.deepcopy(board)

        for num in order:
            state = False
            break_point = True

            while break_point:
                break_point = True
                cnt += 1
                for _ in range(len(dq)):
                    now = dq.popleft()

                    # ENTER
                    if num == nboard[now[0]][now[1]] and not state:
                        state = True
                        nboard[now[0]][now[1]] = 0
                        dq = deque([now])
                        break

                    elif num == nboard[now[0]][now[1]] and state:
                        nboard[now[0]][now[1]] = 0
                        dq = deque([now])
                        break_point = False
                        break

                    # end ENTER

                    # 1칸
                    for i in range(4):
                        tmpx, tmpy = now[0] + dx[i], now[1] + dy[i]
                        if 0 <= tmpx < 4 and 0 <= tmpy < 4 and [tmpx, tmpy] not in dq:
                            dq.append([tmpx,tmpy])

                    # 끝까지
                    for i in range(4):
                        tmpx, tmpy = now[0], now[1]
                        for _ in range(3):
                            tmpx, tmpy = tmpx+dx[i], tmpy+dy[i]
                            if 0 <= tmpx < 4 and 0 <= tmpy < 4:
                                if nboard[tmpx][tmpy] != 0:
                                    break
                            else:
                                tmpx, tmpy = tmpx-dx[i], tmpy-dy[i]
                                break
                        if [tmpx,tmpy] not in dq and [tmpx, tmpy] != now:
                            dq.append([tmpx, tmpy])

        result = min(result, cnt)

    return result


if __name__ == "__main__":
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0

    print(solution(board,r,c))
