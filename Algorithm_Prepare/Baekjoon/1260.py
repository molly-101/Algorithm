import sys
sys.stdin = open('input.txt','rt')
from collections import deque


def solution(n, v, graph):
    answer = []

    # 1. make return strDfs
    strDfs = [v]
    memo = [0]*(n+1)
    memo[v] = 1
    DFS(v, graph, memo, strDfs)
    answer.append(strDfs)

    # 2. make return strBfs
    strBfs = [v]
    dQ = deque()
    dQ.append(v)
    memo = [0]*(n+1)
    memo[v] = 1

    while dQ:
        tmp = dQ.popleft()
        for i in range(len(graph[tmp])):
            if memo[graph[tmp][i]] == 0:
                memo[graph[tmp][i]] = 1
                dQ.append(graph[tmp][i])
                strBfs.append(graph[tmp][i])

    answer.append(strBfs)
    return answer


def DFS(level, graph, memo, strDfs):
    for i in range(len(graph[level])):
        if memo[graph[level][i]] == 0:
            memo[graph[level][i]] = 1
            strDfs.append(graph[level][i])
            DFS(graph[level][i], graph, memo, strDfs)


if __name__ == "__main__":
    n, m, v = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        node1, node2 = map(int,input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(n):
        graph[i].sort()

    answer = solution(n, v, graph)

    for i in answer:
        print(" ".join(map(str, i)))