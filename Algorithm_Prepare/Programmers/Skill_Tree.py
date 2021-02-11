def solution(skill, skill_trees):
    result = 0
    for tree in skill_trees:
        a = 0
        for i in tree:
            if i in skill:
                if skill[a] != i:
                    break
                else:
                    a += 1
        else:
            result += 1
    return result


if __name__ =="__main__":
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    skill = "CBD"
    print(solution(skill, skill_trees))