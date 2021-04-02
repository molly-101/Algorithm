import sys
from collections import deque
sys.stdin = open('input.txt','rt')


def solution(n, m, tasks):
    graph = [[0]*(n+1) for _ in range(n+1)]
    topology = [0]*(n+1)
    answer = []

    for task in tasks:
        graph[task[0]][task[1]] = 1
        topology[task[1]] += 1

    dQ = deque()

    for i in range(1, len(topology)):
        if topology[i] == 0:
            dQ.append(i)

    while dQ:
        tmp = dQ.popleft()
        answer.append(tmp)

        for i in range(n):
            if graph[tmp][i] == 1:
                topology[i] -= 1
                if topology[i] == 0:
                    dQ.append(i)

    return " ".join(map(str, answer))


if __name__ == "__main__":
    n, m = map(int,input().split())
    tasks = []
    for _ in range(m):
        a, b = map(int, input().split())
        tasks.append([a, b])

    print(solution(n, m, tasks))