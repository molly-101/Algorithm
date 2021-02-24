def solution(gems):
    wanted = len(set(gems))
    dic_gems = {}
    lt, rt = 0, 0
    result = []

    # Two pointer Algorithm: 포인터 두 개를 이용해서 탐색한다( 슬라이딩 윈도우도 비슷하게 )
    for i in range(len(gems)):
        # dictionary 구조를 사용한 이유는 set을 사용해 일일히 구하기 위해서는 더 시간이 오래걸리기 때문
        if gems[i] not in dic_gems:
            dic_gems[gems[i]] = 1
        else:
            dic_gems[gems[i]] += 1

        if len(dic_gems) == wanted:
            if not result:
                result = [lt, rt, rt - lt]

            while lt < rt:
                if len(dic_gems) != wanted:
                    break
                else:
                    if result[2] > rt - lt:
                        result = [lt, rt, rt - lt]

                if dic_gems[gems[lt]] > 1:
                    dic_gems[gems[lt]] -= 1
                else:
                    del dic_gems[gems[lt]]
                lt += 1
        rt += 1

    return [result[0] + 1, result[1] + 1]


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
