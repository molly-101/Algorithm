def solution(stones, k):
    set_stones = sorted(set(stones))
    lt, rt = 0, len(set_stones) - 1
    answer = 0

    while lt <= rt:
        mid = (lt + rt) // 2

        if can_cross(stones, set_stones[mid], k):
            lt = mid + 1
            answer = set_stones[mid]
        else:
            rt = mid - 1

    return answer


def can_cross(stones, num, k):  # return Boolean value ( True or False )
    # use mid value
    blank = 0
    for i in stones:
        if i < num:
            blank += 1
        else:
            blank = 0

        if blank == k:
            return False

    return True


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))