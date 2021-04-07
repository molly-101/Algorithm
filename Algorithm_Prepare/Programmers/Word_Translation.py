from collections import deque


def solution(begin, target, words):
    duple = {begin:True}
    dQ = deque()
    dQ.append(begin)
    answer = 0

    while dQ:
        answer += 1
        for i in range(len(dQ)):
            now = dQ.popleft()
            for word in words:
                if word not in duple and is_one_diff(now, word):
                    dQ.append(word)
                    duple[word] = True
                    if word == target:
                        return answer

    return 0


def is_one_diff(word1, word2):
    dif = 0
    for i, j, in zip(word1,word2):
        if i != j:
            dif += 1
    if dif == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))