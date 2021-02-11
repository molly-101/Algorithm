def solution(k):
    segment = [6,2,5,5,4,5,6,3,7,6]
    word = []
    result = [0]

    def DFS(k, cost):
        if word and word[0] == 0: # 맨앞자리 0일때 0 제외 다 되돌아가기
            return
        if cost > k:
            return
        if cost == k:  # clear
            result[0] += 1
        else:
            for i in range(10):
                word.append(i)
                DFS(k, cost + segment[i])
                word.pop()
    DFS(k,0)
    print(result)


if __name__ == "__main__":
    r = [5,6,11,1, 25]
    for i in r:
        print(solution(i))