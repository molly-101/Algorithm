import sys
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    N, weight = map(int,input().split())
    res = [list(map(int,input().split())) for _ in range(N)]
    print(res)
    dy = [0]*(weight+1)
    for i in res:
        for j in range(i[0],weight+1):
            if dy[j] < dy[j-i[0]] + i[1]:
                dy[j] = dy[j-i[0]]+ i[1]
    print(dy[weight])