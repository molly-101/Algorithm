def solution(words, queries):
    Trie = {'num': {}}
    RTrie = {'num': {}}
    result = []

    # Insert word in Trie and RTrie
    for word in words:
        insertTrie(word, Trie, RTrie)

    # find result
    for querie in queries:
        if querie[0] == "?":
            result.append(returnResult("".join(reversed(querie)), RTrie))
        else:
            result.append(returnResult(querie, Trie))

    return result


def returnResult(querie, T):
    now = T
    for i in querie:
        if i == "?" and len(querie) in now['num']:
            return now['num'][len(querie)]
        else:
            if i not in now:
                return 0
            now = now[i]

    return now["num"][len(querie)]


def insertTrie(word, Trie, RTrie):
    now = Trie
    l_word = len(word)
    if l_word not in now['num']:
        now['num'][l_word] = 1
    else:
        now['num'][l_word] += 1
    for i in word:
        if i not in now:
            now[i] = {"num": {l_word: 1}}
        else:
            if l_word not in now[i]['num']:
                now[i]["num"][l_word] = 1
            else:
                now[i]["num"][l_word] += 1

        now = now[i]

    now = RTrie
    if l_word not in now['num']:
        now['num'][l_word] = 1
    else:
        now['num'][l_word] += 1
    for i in reversed(word):
        if i not in now:
            now[i] = {"num": {l_word: 1}}
        else:
            if l_word not in  now[i]["num"]:
                now[i]["num"][l_word] = 1
            else:
                now[i]["num"][l_word] += 1

        now = now[i]


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????", "?????????"]
    print(solution(words,queries))