def solution(n):
    ch = [0] * (n + 1)
    ch[1] = 1
    ch[2] = 2

    for i in range(3, n + 1):
        ch[i] = ch[i - 1] + ch[i - 2]
    return ch[n] % 1000000007


if __name__ == "__main__":
    print(solution(100000))