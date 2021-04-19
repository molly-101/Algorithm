from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    memo = [True] * (n + 1)
    memo[1] = False

    # make graph
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    # BFS graph's node
    dq = deque([1])
    endCnt = 1

    while dq:
        answer = []
        for _ in range(len(dq)):
            now = dq.popleft()
            for i in graph[now]:
                if memo[i]:
                    memo[i] = False
                    dq.append(i)
                    answer.append(i)
                    endCnt += 1

        if endCnt == n:
            break

    return len(answer)


if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))