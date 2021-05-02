import heapq


def solution(ads):
    time, result = 0,0
    ads = sorted(ads, key=lambda x: (x[0], x[1]))

    while ads:
        heap = []
        for ad in ads:
            if time >= ad[0]:
                heapq.heappush(heap, (-ad[1], [ad[0], ad[1]]))
            else:
                break

        if not heap:
            saveAd = ads.pop(0)
            time = saveAd[0] + 5
        else:
            saveAd = heapq.heappop(heap)
            result += saveAd[1][1]*(time - saveAd[1][0])
            time += 5
            ads.remove(saveAd[1])

    return result


if __name__ == "__main__":
    jobs = [[1, 3], [3, 2], [5, 4]]
    print(solution(jobs))