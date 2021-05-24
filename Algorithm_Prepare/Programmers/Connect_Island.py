def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    graph = [[float('inf')] * n for _ in range(n)]
    result = 0

    for i in range(n):
        graph[i][i] = 0

    for cost in costs:
        if floyd_warshall(cost, graph, n):
            result += cost[2]

        for i in graph[0]:
            if i == float('inf'):
                break
        else:
            return result


def floyd_warshall(cost, graph, n):
    if graph[cost[0]][cost[1]] == float('inf'):
        graph[cost[0]][cost[1]] = cost[2]
        graph[cost[1]][cost[0]] = cost[2]
    else:
        return False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    return True