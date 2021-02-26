import sys
sys.stdin = open('input.txt','rt')


def closestStraightCity(c, x, y, q):
    name_dic = {}
    dx = {}
    dy = {}
    # dictionary(sorted map) 이중 해시로 만든다
    for i, j, k in zip(c,x,y):
        name_dic[i] = [j,k]
        if j not in dx:
            dx[j] = {}
            dx[j][k] = i
        else:
            dx[j][k] = i
        if k not in dy:
            dy[k] = {}
            dy[k][j] = i
        else:
            dy[k][j] = i

    for i in q: # 여기서 i 는 기준이 되는 곳 또는 찾아야 할 곳
        result = ["NAME", float('inf')]  # result 에서 0번 index 에는 이름, 1번 인덱스에는 최대 거리를 넣어준다 ( 작은 걸 찾으니까 )
        tmp = name_dic[i]  # 찾아야 할 곳의 이름을 바탕으로 dictionary 에서 "좌표" 를 저장
        tmpx, tmpy = dx[tmp[0]],dy[tmp[1]]

        # X 와 Y의 값이 의미: 찾아야할 좌표의 index 위치를 각각 갖는다.
        X, Y = list(tmpx).index(tmp[1]), list(tmpy).index(tmp[0])

        # for 루프 안에서 계속 len 함수를 실행하면 complexity 가 높아지니 밖에서 미리 구해주자.
        lenx, leny = len(tmpx),len(tmpy)

        # 기준이 되는 좌표에서 -1 한 인덱스의 값과 +1 한 인덱스의 값을 비교하기 위해서 move 생성.
        move = [-1,1]
        for j in move:
            # 기준 좌표에서 +1, -1 인덱스 떨어진 좌표까지의 거리와 result 에 저장된 거리 비교해서 더 작은값 저장!
            if 0 <= X+j <lenx:
                if abs(list(tmpx.keys())[X+j] - tmp[1]) < result[1]:
                    result = [tmpx[list(tmpx.keys())[X+j]], abs(list(tmpx.keys())[X+j] - tmp[1])]
            if 0 <= Y+j <leny:
                if abs(list(tmpy.keys())[Y+j] - tmp[0]) < result[1]:
                    result = [tmpy[list(tmpy.keys())[Y+j]], abs(list(tmpy.keys())[Y+j] - tmp[0])]

        # result 가 매우 크다 -> 변화가 없다 -> NONE
        if result[1] > 1000000000:
            print("NONE")
        else:
            print(result)


if __name__ == "__main__":
    c = []
    x = []
    y = []
    q = []
    for i in range(int(input())):
        c.append(str(input()))
    for i in range(int(input())):
        x.append(int(input()))
    for i in range(int(input())):
        y.append(int(input()))
    for i in range(int(input())):
        q.append(str(input()))
    closestStraightCity(c,x,y,q)