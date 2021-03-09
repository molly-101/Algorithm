def solution(land):
    memo = land[0]
    if len(land) == 1:
        return max(memo)

    for i in land[1:]:
        tmp = [0,0,0,0]
        for j in range(4):
            if j == 0:
                tmp[j] = max(memo[1], memo[2], memo[3]) + i[j]
            elif j == 1:
                tmp[j] = max(memo[0], memo[2], memo[3]) + i[j]
            elif j == 2:
                tmp[j] = max(memo[0], memo[1], memo[3]) + i[j]
            else:
                tmp[j] = max(memo[0], memo[1], memo[2]) + i[j]

        memo = tmp

    return max(memo)


if __name__ == "__main__":
    land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
    print(solution(land))