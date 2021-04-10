from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    duple = {}

    # start setting
    dQ = deque()
    dQ.append(1)
    duple[1] = True

    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    answer = 0
    while dQ:
        answer = len(dQ)
        for _ in range(len(dQ)):
            tmp = dQ.popleft()
            for i in graph[tmp]:
                if i not in duple:
                    duple[i] = True
                    dQ.append(i)

    return answer

if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))