from collections import deque
import copy


def solution(n, start, end, roads, traps):
    # init graph
    graph = [[] for _ in range(n+1)]
    result = float('inf')

    for i in roads:
        graph[i[0]].append([i[1], i[2], True])
        graph[i[1]].append([i[0], i[2], False])

    dq = deque([[start, copy.deepcopy(graph), 0]])

    while dq:
        tmp = dq.popleft()
        for i in tmp[1][tmp[0]]:
            if i[2] and i[0] == end:
                result = min(result, tmp[2]+i[1])
                continue

            if i[2] and i[0] not in traps and result > tmp[2]+i[1]:
                dq.append([i[0], tmp[1], tmp[2]+i[1]])
            elif i[2] and i[0] in traps and result > tmp[2]+i[1]:
                target = i[0]
                for idx, j in enumerate(tmp[1]):
                    for idx2, k in enumerate(j):
                        if target == k[0] and not k[2]:
                            tmp[1][idx][idx2][2] = True
                        elif target == k[0] and k[2]:
                            tmp[1][idx][idx2][2] = False
                        if target == idx and k[2]:
                            tmp[1][idx][idx2][2] = False
                        elif target == idx and not k[2]:
                            tmp[1][idx][idx2][2] = True
                dq.append([i[0], tmp[1], tmp[2]+i[1]])

    return result

if __name__ == "__main__":
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2,3]
    print(solution(n,start,end, roads, traps))