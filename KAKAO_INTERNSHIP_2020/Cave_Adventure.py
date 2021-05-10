from collections import deque
import copy


def solution(n, path, order):
    # make path board
    board = [[] for _ in range(n)]
    # memorize Topological list
    prior_list = [0] * n
    # 방문하면 열리는 곳
    order_list = [0] * n
    # 방문한 곳 체크
    memo = [0] * n

    # path insert
    for route in path:
        board[route[0]].append(route[1])
        board[route[1]].append(route[0])
    # prior insert
    for i in order:
        prior_list[i[1]] = 1
        order_list[i[0]] = i[1]

    dQ = deque()
    dQ.append(0)
    if prior_list[0] == 1:
        return False

    while dQ:
        dif = copy.deepcopy(dQ)

        for _ in range(len(dQ)):
            tmp = dQ.popleft()
            prior_list[order_list[tmp]] = 0

            if prior_list[tmp] != 0:
                dQ.append(tmp)
            else:
                memo[tmp] = 1
                for i in board[tmp]:
                    if memo[i] == 0:
                        dQ.append(i)

        if dif == dQ:
            return False

    return True