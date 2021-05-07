def solution(stones, k):
    # initialize set type stones and binary search
    s_stones = list(sorted(set(stones)))
    lt, rt = 0, len(s_stones) - 1
    result = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        blank = 0
        state = True
        for stone in stones:
            if stone - s_stones[mid] < 0:
                blank += 1
            else:
                blank = 0

            if blank == k:
                state = False
                break

        if state:
            result = max(result, s_stones[mid])
            lt = mid + 1
        else:
            rt = mid - 1

    return result


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))