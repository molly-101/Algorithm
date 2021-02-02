def solution(genres, plays):
    res = {}
    cnt = 0

    for genre, play in zip(genres,plays):
        if genre not in res:
            res[genre] = {}
            if play not in res[genre]:
                res[genre][play] = [cnt]
        else:
            if play not in res[genre]:
                res[genre][play] = [cnt]
            else:
                res[genre][play].append(cnt)
        cnt += 1

    n_res = sorted(res.items(),key=lambda x:sum(x[1]),reverse=True)

    res = []
    for i in n_res:
        a = sorted(i[1].items(), key=lambda x:x[0],reverse=True)
        res.append(a)
    result = []
    for i in res:
        cnt = 0
        for j in i:
            for k in sorted(j[1]):
                if cnt < 2:
                    result.append(k)
                    cnt += 1
                else:
                    break
            if cnt >= 2:
                break
    return result



if __name__ == "__main__":
    genres = ["classic","pop","classic","classic","pop"]
    plays = [500,600,150,800,2500]
    print(solution(genres,plays))
