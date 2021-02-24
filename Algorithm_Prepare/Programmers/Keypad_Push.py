def solution(numbers, hand):
    res = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]
    now_L, now_R = 10, 11
    result = ""

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            now_L = number
            result += "L"
        if number == 3 or number == 6 or number == 9:
            now_R = number
            result += "R"
        if number == 2 or number == 5 or number == 8 or number == 0:
            if find_distance(res[number], res[now_L]) < find_distance(res[number], res[now_R]):
                now_L = number
                result += "L"
            elif find_distance(res[number], res[now_L]) > find_distance(res[number], res[now_R]):
                now_R = number
                result += "R"
            else:
                if hand == "left":
                    now_L = number
                    result += "L"
                else:
                    now_R = number
                    result += "R"
    return result


def find_distance(l1, l2):
    return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])


if __name__ =="__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(numbers,hand))