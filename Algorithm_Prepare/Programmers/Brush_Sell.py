def solution(enroll, referral, seller, amount):
    # 1. make res and result
    res, result = {}, {}
    for e, r in zip(enroll, referral):
        res[e] = r
        result[e] = 0

    # selling
    for s, a in zip(seller, amount):
        now = s
        a = a*100

        while now != "-":
            tmp = int(a//10)
            result[now] += a-tmp
            now = res[now]
            a = tmp

    return list(result.values())


if __name__ == "__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    print(solution(enroll,referral,seller,amount))