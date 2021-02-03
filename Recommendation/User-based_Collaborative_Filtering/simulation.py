import sys
import math
sys.stdin = open('input.txt', 'rt')


def rate_average(U, usr):
    cnt, result = 0,0
    for r in U[usr]:
        if r != 0:
            result += r
            cnt += 1
    return result/cnt


def calc_similarity(normalized, user1, user2):
    if user1 == user2:
        return 1
    else:
        return sum(u1*u2 for u1, u2 in zip(normalized[user1], normalized[user2]))


def find_rate_i(user, i):  # U[user-1][i]는 0이여야 접근할 수 있다. prime_u 또한 값을 매겨야 한다.
    num = 0
    for prime_u in U_prime:
        if U[prime_u][i] != 0:
            simil = similarity[user - 1][prime_u][0]
            avg_prime_u_rate = rate_average(U, prime_u)
            rate_prime_u_i = U[prime_u][i]
            num += simil * float(rate_prime_u_i - avg_prime_u_rate)

    return num


if __name__ == "__main__":
    # 변수 설정
    num_sim_user_topk = int(input()) # 식 (2)으로 계산할 U' 에 쓰일 최근접 이웃 사용자 수
    num_item_rec_topk = int(input()) # 출력 할 추천 결과의 개수
    num_users = int(input()) # 전체 유저 수
    num_items = int(input()) # 전체 아이템 수
    num_rows = int(input()) # 매긴 점수의 가짓 수

    # user: 행, item: 열
    # U : 모든 u 들의 rate를 저장한 리스트, normalized: 코사인 정규화한 리스트(similar)에 쓰인다.
    U = [[0]*num_items for _ in range(num_users)]
    normalized = [[0]*num_items for _ in range(num_users)]
    # rows 만큼 반복해서 점수 입력 후 정규화
    for i in range(num_rows):
        user, item, grade = map(float, input().split())
        U[int(user)-1][int(item)-1] = grade  # User와 item은 1 부터 시작하기 때문에 -1씩 해주어야 한다

    for i in range(num_users):
        den = math.sqrt(sum(pow(U[i][k],2) for k in range(num_items))) #분자
        for j in range(num_items):
            if U[i][j] != 0:
                normalized[i][j] = U[i][j]/den

    # similarity: user i와 j에 대하여 모든 유사도를 [유사도, 인덱스] 로 가지고 있는 리스트
    similarity = [[0]*num_users for _ in range(num_users)]
    for i in range(num_users):
        for j in range(num_users):
            similarity[i][j] = [calc_similarity(normalized,i,j),j]

    num_reco_users = int(input())
    # num_reco_users 만큼 입력받아서 계산 후 출력
    for i in range(num_reco_users):
        user = int(input())  # 이 user에 맞는 작품을 추천할 것이다
        # 완전히 똑같은 점수를 준 user가 없다고 가정한다
        res = sorted(similarity[user-1], key=lambda x:x[0], reverse=True)

        U_prime = []

        for i in range(1,num_sim_user_topk+1):
            U_prime.append(res[i][1])

        avg_user_rate = rate_average(U, user-1) # user의 rate average

        den = sum(similarity[user-1][i][0] for i in U_prime)
        result = []
        for i in range(num_items):
            if U[user-1][i] == 0:
                #print("avg_user_rate: ", avg_user_rate, " 분모: ", find_rate_i(user,i), "분자:", den, find_rate_i(user,i)/den)
                r_i = avg_user_rate + find_rate_i(user, i)/den

                # result 에 append 할 때는 적어도 하나의 값이 들어왔을때이다. 보다 안정성 있게 바꾸려면 생각을 해야할듯 0점을 못넣게됨 지금 방식은.
                if r_i != avg_user_rate:
                    result.append([i,r_i])
        tmp = sorted(result,key=lambda x:x[1],reverse=True)

        # 결과 값 출력: num_item_rec_topk 개수만큼 tmp에서 출력합니다.
        for i in range(len(tmp)):
            if i < num_item_rec_topk:
                print(tmp[i][0]+1, end= " ")
        print()




