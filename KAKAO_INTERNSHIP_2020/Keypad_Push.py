def solution(numbers, hand):
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1], "*": [3, 0], "#": [3, 2]}
    handDic = {"left": "L", "right": "R"}
    left, right = "*", "#"
    result = ""

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left = i
            result += "L"
        elif i == 3 or i == 6 or i == 9:
            right = i
            result += "R"
        else:
            t_hand = returnNearHand(left, right, i, dic, hand)
            result += handDic[t_hand]
            if handDic[t_hand] == "L":
                left = i
            else:
                right = i

    return result


def returnNearHand(left, right, goal, dic, hand):
    if abs(dic[left][0] - dic[goal][0]) + abs(dic[left][1] - dic[goal][1]) < abs(dic[right][0] - dic[goal][0]) + abs(dic[right][1] - dic[goal][1]):
        return "left"
    elif abs(dic[left][0] - dic[goal][0]) + abs(dic[left][1] - dic[goal][1]) > abs(dic[right][0] - dic[goal][0]) + abs(dic[right][1] - dic[goal][1]):
        return "right"
    else:
        return hand


if __name__ == "__main__":
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    print(solution(numbers, hand))