def solution(k, room_number):
    memo = {}
    result = []

    for num in room_number:
        if memo.get(num, 0) == 0:
            memo[num] = num + 1
        else:
            tmp = [num]  # save route

            while memo.get(num, 0) != 0:
                num = memo[num]
                tmp.append(num)

            for i in tmp:
                memo[i] = num + 1

            memo[num] = num + 1

        result.append(num)

    return result