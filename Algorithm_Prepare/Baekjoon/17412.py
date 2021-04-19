import sys
sys.stdin = open('input.txt','rt')


def DFS(level, graph):
    global state, answer

    if level == 2:
        answer += 1
        state = True
    else:
        for i in range(len(graph[level])):
            tmp = graph[level].pop()
            DFS(tmp, graph)
            if state:
                return
            else:
                graph[level].insert(0, tmp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    answer = 0

    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)

    state = False

    for i in range(len(graph[1])):
        DFS(graph[1][i], graph)
        state = True

    print(answer)