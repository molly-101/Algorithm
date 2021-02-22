def solution(n, s, a, b, fares):
    dist = [[20000000] * (n + 1) for _ in range(n + 1)]

    # make 0 point
    for i in range(n + 1):
        dist[i][i] = 0

    # make fares point
    for fare in fares:
        dist[fare[0]][fare[1]] = fare[2]
        dist[fare[1]][fare[0]] = fare[2]

    # floyd warshall algorithm
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

    # find shortest path
    tmp = float('inf')
    for i in range(1, n + 1):
        tmp = min(dist[s][i] + dist[i][a] + dist[i][b], tmp)
    return tmp