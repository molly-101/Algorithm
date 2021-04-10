def solution(nodeinfo):
    preorder, postorder = [],[]

    # node information -> [x, y, node_num, left_c, right_c, parent_num]
    for i in range(1, len(nodeinfo)+1):
        nodeinfo[i-1].append(i)
        nodeinfo[i-1] += [0,0,0]

    nodeinfo = sorted(nodeinfo, key=lambda x: (x[1], -x[0]), reverse=True)

    duple = {}

    node_dict = {}
    for i in nodeinfo:
        node_dict[i[2]] = i
    print(nodeinfo)

    #오류 터지는 부분
    for i in range(len(nodeinfo)):
        for j in range(i+1, len(nodeinfo)):
            if nodeinfo[i][5] == 0:
                if nodeinfo[j][1] < nodeinfo[i][1] and nodeinfo[i][3] == 0 and nodeinfo[j][0] < nodeinfo[i][0] and nodeinfo[j][2] not in duple:
                    nodeinfo[i][3] = nodeinfo[j][2]
                    duple[nodeinfo[j][2]] = True
                    nodeinfo[j][5] = nodeinfo[i][2]
                if nodeinfo[j][1] < nodeinfo[i][1] and nodeinfo[i][4] == 0 and nodeinfo[j][0] > nodeinfo[i][0] and nodeinfo[j][2] not in duple:
                    nodeinfo[i][4] = nodeinfo[j][2]
                    duple[nodeinfo[j][2]] = True
                    nodeinfo[j][5] = nodeinfo[i][2]
            else:
                if nodeinfo[j][1] < nodeinfo[i][1] and nodeinfo[i][3] == 0 and nodeinfo[j][0] < nodeinfo[i][0] and nodeinfo[j][2] not in duple:
                    if nodeinfo[i][0] > nodeinfo[j][0] > node_dict[nodeinfo[i][5]][0] or nodeinfo[i][0] < node_dict[nodeinfo[i][5]][0]:
                        nodeinfo[i][3] = nodeinfo[j][2]
                        duple[nodeinfo[j][2]] = True
                        nodeinfo[j][5] = nodeinfo[i][2]

                if nodeinfo[j][1] < nodeinfo[i][1] and nodeinfo[i][4] == 0 and nodeinfo[j][0] > nodeinfo[i][0] and nodeinfo[j][2] not in duple:
                    if nodeinfo[i][0] < nodeinfo[j][0] < node_dict[nodeinfo[i][5]][0] or nodeinfo[i][0] > node_dict[nodeinfo[i][5]][0]:
                        nodeinfo[i][4] = nodeinfo[j][2]
                        duple[nodeinfo[j][2]] = True
                        nodeinfo[j][5] = nodeinfo[i][2]

            if nodeinfo[i][3] != 0 and nodeinfo[i][4] != 0:
                break
        print(duple)


    start = nodeinfo[0][2]

    print(nodeinfo)
    nodeinfo = sorted(nodeinfo, key=lambda x: x[2])

    DFS(start, preorder, postorder, nodeinfo)

    print(preorder, postorder)

    return [preorder, postorder]


def DFS(level, preorder, postorder, nodeinfo):
    if level == 0:
        return
    else:
        preorder.append(level)
        DFS(nodeinfo[level-1][3], preorder, postorder, nodeinfo)
        DFS(nodeinfo[level-1][4], preorder, postorder, nodeinfo)
        postorder.append(level)




if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

    if solution(nodeinfo) == result:
        print("True")