def solution(n, computers):
    duple = {}
    count = 0

    for i in range(n):
        if i not in duple:
            DFS(i, n, computers, duple)
            count += 1

    return count


def DFS(level, n, computers, duple):
    for i in range(level, n):
        if computers[level][i] == 1 and i not in duple:
            duple[i] = True
            DFS(i, n, computers, duple)


if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))