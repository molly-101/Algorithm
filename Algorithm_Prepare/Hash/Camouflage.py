def solution(clothes):
    dict_clothes = {}

    for clothe in clothes:
        if clothe[1] not in dict_clothes:
            dict_clothes[clothe[1]] = 1
        else:
            dict_clothes[clothe[1]] += 1

    result = 1

    for i in dict_clothes.items():
        result *= (i[1] + 1)

    return result - 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))