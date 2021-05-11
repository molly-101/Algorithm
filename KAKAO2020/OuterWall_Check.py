from itertools import permutations
from collections import deque


def solution(n, weak, dist):
    # update weak point -> point + n
    l_weak = len(weak)
    for i in range(l_weak):
        weak.append(weak[i] + n)

    # make permutations in dist (dist <= 8) can permutations
    p_dist = permutations(dist)

    # return result -> minimum friends from returnMinimumFriends or result
    result = 10

    for permutation in p_dist:
        for i in range(l_weak):
            now = weak[i:i + l_weak]
            result = min(result, returnMinimumFriends(now, permutation))

    if result == 10:
        return -1

    return result


def returnMinimumFriends(now, permutation):
    point = -1
    permutation = deque(permutation)
    cnt = 0

    for i in range(len(now)):
        if point < now[i]:
            if permutation:
                point = now[i] + permutation.popleft()
                cnt += 1
            else:
                break
    else:
        return cnt

    return 10


if __name__ == "__main__":
    n = 200
    weak = [0, 100]
    dist = [1, 1]
    print(solution(n, weak, dist))