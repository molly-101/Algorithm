def solution(lottos, win_nums):
    zeros = 0
    atari = 0
    for i in lottos:
        if i == 0:
            zeros += 1

        if i in win_nums:
            atari += 1
            win_nums.remove(i)

    result = [atari + zeros, atari]

    for i in range(2):
        if result[i] <= 1:
            result[i] = 6
        else:
            result[i] = 7 - result[i]

    return result