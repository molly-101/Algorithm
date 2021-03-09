def solution(n):
    state = 1
    dif = one_count(n)

    while True:
        if one_count(n + state) == dif:
            return state + n
        state += 1


def one_count(k):
    binary_k = bin(k)
    cnt = 0
    for i in binary_k[2:]:
        if i == "1":
            cnt += 1
    print(cnt)
    return cnt


if __name__ == "__main__":
    print(solution(78))