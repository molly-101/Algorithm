def solution(people, limit):
    people = sorted(people, reverse=True)
    lt, rt = 0, len(people) - 1
    answer = 0

    while lt < rt:
        if people[lt] + people[rt] <= limit:
            rt -= 1
            people[lt] += people[rt]
        else:
            lt += 1
            answer += 1

    return answer + 1