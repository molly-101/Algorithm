def solution(gems):
    l_gem_set = len(set(gems))
    gem_dict, lt, result = {}, 0, [0, float('inf')]

    for i in range(len(gems)):
        if gems[i] not in gem_dict:
            gem_dict[gems[i]] = 1
        else:
            gem_dict[gems[i]] += 1

        while len(gem_dict) == l_gem_set:
            if result[1] - result[0] > i - lt:
                result = [lt + 1, i + 1]

            gem_dict[gems[lt]] -= 1

            if gem_dict[gems[lt]] == 0:
                del gem_dict[gems[lt]]

            lt += 1

    return result


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))