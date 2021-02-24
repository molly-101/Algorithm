import copy


def solution(info, query):
    information = {}
    for i in info:
        language, part, career, food, point = map(str, i.split())
        if language not in information:
            information[language] = {}
        if part not in information[language]:
            information[language][part] = {}
        if career not in information[language][part]:
            information[language][part][career] = {}
        if food not in information[language][part][career]:
            information[language][part][career][food] = [int(point)]
        else:
            information[language][part][career][food].append(int(point))

    def DFS(level, inform, q, point):

        if level == 0: # language
            if q[0] == "-":
                if 'python' in inform:
                    DFS(level+1,inform['python'], q, point)
                if 'cpp' in inform:
                    DFS(level + 1, inform['cpp'], q, point)
                if 'java' in inform:
                    DFS(level + 1, inform['java'], q,point)
            else:
                if q[level] in inform:
                    DFS(level + 1, inform[q[level]], q,point)
        elif level == 1: # part
            if q[1] == "-":
                if 'backend' in inform:
                    DFS(level + 1, inform['backend'], q,point)
                if 'frontend' in inform:
                    DFS(level + 1, inform['frontend'], q,point)
            else:
                if q[level] in inform:
                    DFS(level + 1, inform[q[level]], q,point)
        elif level == 2: # career
            if q[2] == "-":
                if 'junior' in inform:
                    DFS(level + 1, inform['junior'], q,point)
                if 'senior' in inform:
                    DFS(level + 1, inform['senior'], q,point)
            else:
                if q[level] in inform:
                    DFS(level+1,inform[q[level]],q,point)
        elif level == 3: # food
            if q[3] == "-":
                if 'chicken' in inform:
                    DFS(level + 1, inform['chicken'], q,point)
                if 'pizza' in inform:
                    DFS(level + 1, inform['pizza'], q,point)
            else:
                if q[level] in inform:
                    DFS(level + 1, inform[q[level]], q,point)
        else:
            for i in inform:
                if i >= point:
                    li[0] += 1

    result = []
    for i in query:
        q = i.split()
        li = [0]
        for _ in range(3):
            q.remove("and")
        DFS(0,information,q, int(q[4]))
        result.append(li[0])
    return result




if __name__ == "__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info,query))