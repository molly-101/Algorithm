from collections import deque
from itertools import permutations
import copy


def solution(board, r, c):
    maximum = boardMaxCnt(board)
    cards = [i for i in range(1, maximum + 1)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    result = float('inf')

    for order in permutations(cards):  # card 뽑을 순서에 대한 순열
        move_count = 0  # 여기 있어야 count마다 비교할 수 있다
        copyboard = copy.deepcopy(board)  # copy board to use onetime
        nows = deque()
        nows.append([r, c])
        for card in order:  # (1,2,3), (2,1,3)과 같은 카드 뽑는 순서
            # card pair 를 BFS
            pair = 0

            while pair != 2:  # find one pair cards
                move_count += 1

                for _ in range(len(nows)):
                    now = nows.popleft()
                    check_duple = [[0] * 4 for _ in range(4)]
                    check_duple[now[0]][now[1]] = 1

                    # 현재 위치가 card와 같을 경우 ENTER
                    if copyboard[now[0]][now[1]] == card and pair == 0:  # first card
                        pair += 1
                        nows = deque()  # 초기화
                        nows.append(now)
                        copyboard[now[0]][now[1]] = 0
                        break
                    if copyboard[now[0]][now[1]] == card and pair == 1:  # second card
                        pair += 1
                        nows = deque()
                        nows.append(now)
                        copyboard[now[0]][now[1]] = 0
                        break

                    # Ctrl move
                    for i in range(4):
                        tmpx, tmpy = now[0], now[1]
                        for _ in range(3):
                            tmpx, tmpy = tmpx + dx[i], tmpy + dy[i]
                            if 0 <= tmpx <= 3 and 0 <= tmpy <= 3 and check_duple[tmpx][tmpy] == 0:
                                if i == 0:  # upside
                                    if tmpx == 0 or copyboard[tmpx][tmpy] != 0:
                                        nows.append([tmpx, tmpy])
                                        check_duple[tmpx][tmpy] = 1
                                        break
                                elif i == 1:  # right
                                    if tmpy == 3 or copyboard[tmpx][tmpy] != 0:
                                        nows.append([tmpx, tmpy])
                                        check_duple[tmpx][tmpy] = 1
                                        break
                                elif i == 2:  # down
                                    if tmpx == 3 or copyboard[tmpx][tmpy] != 0:
                                        nows.append([tmpx, tmpy])
                                        check_duple[tmpx][tmpy] = 1
                                        break
                                elif i == 3:  # left
                                    if tmpy == 0 or copyboard[tmpx][tmpy] != 0:
                                        nows.append([tmpx, tmpy])
                                        check_duple[tmpx][tmpy] = 1
                                        break
                    # 1 block move
                    for i in range(4):
                        tmpx, tmpy = now[0] + dx[i], now[1] + dy[i]
                        if 0 <= tmpx <= 3 and 0 <= tmpy <= 3 and check_duple[tmpx][tmpy] == 0:
                            nows.append([tmpx, tmpy])
                            check_duple[tmpx][tmpy] = 1
        if result > move_count:
            result = move_count
    return result


def boardMaxCnt(board):
    maximum = 0
    for i in board:
        for j in i:
            if maximum < j:
                maximum = j
    return maximum


if __name__ == "__main__":
    board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
    r = 1
    c = 0
    print(solution(board,r,c))