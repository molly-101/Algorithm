def solution(genres, plays):
    res = {}
    cnt = 0

    # genres, plays 를 zip으로 묶어 딕셔너리에 저장
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

    # 장르별로 플레이한 총 회수에 대하여 정렬한 리스트 생성
    n_res = sorted(res.items(),key=lambda x:sum(x[1]),reverse=True)

    res = []
    # 장르 내에서 많이 재생한 순으로 재정렬
    for i in n_res:
        a = sorted(i[1].items(), key=lambda x:x[0],reverse=True)
        res.append(a)

    # result 리스트에 2개씩 넣어주기 위한 동작과정 중복 횟수가 있을 수 있으니 정렬하면서 접근
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
