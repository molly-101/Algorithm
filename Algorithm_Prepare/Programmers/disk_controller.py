import heapq
from collections import deque


def solution(jobs):
    jobs = deque(sorted(jobs, key=lambda x: (x[0],x[1])))
    now, length = 0, len(jobs)
    hq = []
    result = 0

    while jobs or hq:
        while jobs and now >= jobs[0][0]:
            tmp = jobs.popleft()
            heapq.heappush(hq, [tmp[1], tmp])
        if not hq:
            tmp = jobs.popleft()
            now = tmp[0] + tmp[1]
            result += tmp[1]
        else:
            tmp = heapq.heappop(hq)
            result += now - tmp[1][0] + tmp[1][1]
            now += tmp[0]

    return result // length


if __name__ == "__main__":
    jobs = [[0,3], [1,9],[2,6]]
    print(solution(jobs))