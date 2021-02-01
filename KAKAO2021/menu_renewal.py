courseList = {}


def solution(orders, course):
    ch = [[] for _ in range(11)]
    for order in orders:
        DFS(0,"",course,sorted(order))
    # 더 좋은 방법을 찾기에는 시간이 오래걸림 분명 더 좋은 방법이 있을것이다.
    collections = sorted(courseList.items(), key=lambda x:x[1], reverse=True)
    for collection in collections:
        if collection[1] > 1:
            if not ch[len(collection[0])]:
                ch[len(collection[0])].append(collection)
            else:
                if ch[len(collection[0])][0][1] == collection[1]:
                    ch[len(collection[0])].append(collection)
    result = []

    #비효율적이므로 개선 필요.
    for i in ch:
        if i:
            for j in i:
                result.append(j[0])
    return sorted(result)


def DFS(level,sample, course, order):
    # closing part
    if level == len(order):
        if len(sample) in course:
            if sample not in courseList:
                courseList[sample] = 1
            else:
                courseList[sample] += 1
    else:
        DFS(level+1,sample + order[level], course, order)
        DFS(level + 1, sample, course, order)


if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders,course))
