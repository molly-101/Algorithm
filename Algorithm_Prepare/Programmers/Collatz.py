
def solution(num):
    result = 0
    for i in range(500):
        if num == 1:
            return result
        if num%2 == 0:
            num //= 2
            result += 1
            continue
        else:
            num *= 3
            num += 1
            result += 1
    else:
        return -1


if __name__ == "__main__":
    print(solution(6))