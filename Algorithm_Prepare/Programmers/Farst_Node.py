from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    duple = [True] * (n + 1)
    duple[1] = False

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    dq = deque([1])
    result = []
    cnt = 0

    while dq:
        cnt = 0
        for _ in range(len(dq)):
            now = dq.popleft()
            for i in graph[now]:
                if duple[i]:
                    dq.append(i)
                    duple[i] = False
                    cnt += 1
        result.append(cnt)

    return result[-2]