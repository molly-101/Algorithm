from itertools import permutations


def solution(n, weak, dist):
    # 1. append n+weak point
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    # 2. sort dist
    dist = sorted(dist, reverse=True)

    # 3. find answer
    slide_size = len(weak) // 2
    answer = float('inf')
    l_dist = len(dist)

    for i in range(slide_size):
        for dis in permutations(dist):
            slide = weak[i:i + slide_size]
            answer = min(answer, search_weak(slide, dis, l_dist))

    if answer == 100000000:
        return -1
    else:
        return answer


# return how many people for find search weakness (int)
def search_weak(slide, dis, l_dist):
    state = -1
    mans = 0
    point = 0

    for i in slide:
        if point == l_dist:
            return 100000000
        if state < i:
            state = i + dis[point]
            mans += 1
            point += 1

    return mans


if __name__ == "__main__":
    n = 200
    weak = [0,100]
    dist = [1,2,3,4]
    print(solution(n, weak, dist))