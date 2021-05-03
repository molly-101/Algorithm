def solution(user_id, banned_id):
    # make hashmap
    banned_dic = [set() for _ in range(len(banned_id))]

    # input user_id in hashmap
    for i in user_id:
        for j in range(len(banned_id)):
            if len(i) == len(banned_id[j]):
                for u, b in zip(i, banned_id[j]):
                    if b != "*" and u != b:
                        break
                else:
                    banned_dic[j].add(i)

    # make result
    result = set()
    values = banned_dic
    li = []
    DFS(0, values, li, result)

    return len(result)


def DFS(level, values, li, result):
    if level == len(values):
        result.add("".join(sorted(li)))
    else:
        for i in values[level]:
            if i not in li:
                li.append(i)
                DFS(level + 1, values, li, result)
                li.pop()


if __name__ == "__main__":
    user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id =["*rodo", "*rodo", "******"]
    print(solution(user_id,banned_id))