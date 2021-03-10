def solution(n, words):
    duple = {}
    now = 0
    state = words[0][0]

    for word in words:
        if state == word[0] and word not in duple:
            duple[word] = 1
            state = word[-1]
            now += 1
        else:
            print(duple, state, word[0])
            return [(now % n) + 1, now // n + 1]

    else:
        return [0, 0]


if __name__ == "__main__":
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    print(solution(3, words))