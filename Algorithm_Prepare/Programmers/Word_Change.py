from collections import deque


def solution(begin, target, words):
    # make words dictionary to use duplicate
    w_dict = {}
    for word in words:
        w_dict[word] = True

    w_dict[begin] = False

    dq = deque([begin])

    # BFS search
    result = 0

    while dq:
        result += 1
        for i in range(len(dq)):
            now = dq.popleft()
            for word in words:
                if w_dict[word] and one_difference(word, now):
                    dq.append(word)
                    w_dict[word] = False
                    if word == target:
                        return result

    return 0


def one_difference(w1, w2):
    cnt = 0
    for i, j in zip(w1, w2):
        if i != j:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False