def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    return max(collect_sticker(sticker[1:]), collect_sticker(sticker[:-1]))


def collect_sticker(sticker):
    l_sticker = len(sticker)
    memo = [0] * l_sticker
    memo[0], memo[1], memo[2] = sticker[0], sticker[1], sticker[0] + sticker[2]
    rt_max = max(memo[:3])

    for i in range(3, l_sticker):
        memo[i] = max(memo[i - 2], memo[i - 3]) + sticker[i]
        if memo[i] > rt_max:
            rt_max = memo[i]
    return rt_max


if __name__ == "__main__":
    sticker = [14, 6, 5, 11, 3, 9, 2, 10]
    print(solution(sticker))