def solution(numbers, target):
    result = [0]
    DFS(0, numbers, target, 0, result)
    return result[0]


def DFS(level, numbers, target, now, result):
    if level == len(numbers):
        if now == target:
            result[0] += 1
    else:
        DFS(level+1, numbers, target, now+numbers[level], result)
        DFS(level+1, numbers, target, now-numbers[level], result)


if __name__ == "__main__":
    numbers = [1,1,1,1,1]
    target = 3
    print(solution(numbers, target))