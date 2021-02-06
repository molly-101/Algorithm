from collections import deque


# level3
def solution(n, edge):
    res = [[] for _ in range(n+1)]
    duple = [0]*(n+1)
    # make resource
    for i in edge:
        res[i[0]].append(i[1])
        res[i[1]].append(i[0])

    Q = deque()
    Q.append(1)
    # duplicated node checker: duple
    duple[1] = 1
    # return value
    result = 0

    # BFS searching
    while Q:
        for i in range(len(Q)):
            tmp_Q = Q.popleft()
            for j in res[tmp_Q]:
                if duple[j] == 0:
                    Q.append(j)
                    duple[j] = 1
        if Q:
            result = len(Q)

    return result



if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    solution(n, edge)