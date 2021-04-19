def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ranks = [[1, 0], [2, 0], [3, 0]]

    for idx, answer in enumerate(answers):
        if answer == supo1[idx % 5]:
            ranks[0][1] += 1
        if answer == supo2[idx % 8]:
            ranks[1][1] += 1
        if answer == supo3[idx % 10]:
            ranks[2][1] += 1

    ranks = sorted(ranks, key=lambda x: (x[1], -x[0]), reverse=True)
    now, answer = ranks[0][1], []

    for rank in ranks:
        if now == rank[1]:
            answer.append(rank[0])

    return answer


if __name__ == "__main__":
    answers = [1,3,2,4,2]
    print(solution(answers))