from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0

    for i in cities:
        city = i.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time +=5

    return time


if __name__ == "__main__":
    cacheSize =0
    cities =["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))