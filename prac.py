import sys
sys.stdin = open('input.txt')


for ir in range(int(input())):
    V, E = map(int, input().split())
    visit = list(0 for i in range(V+1))
    v_num = 0

    visit[0] = 1
    point = list(list(0 for i in range(V+1)) for i1 in range(V+1))
    for i1 in range(E):
        i, j, w = map(int, input().split())
        point[i][j] = w
        point[j][i] = w
    result = 0
    start = 0
    move = []
    v1 = 0
    while True:
        for i in range(V+1):
            if point[start][i] != 0 and visit[i] == 0:
                q = 0
                if not move:
                    move.append([i, point[start][i]])

                else:
                    mer = point[start][i]
                    for idx, ii in enumerate(move):
                        if ii[1] > mer:
                            move.insert(idx, [i, mer])
                            break
                    else:
                        move.append([i, point[start][i]])

        p1 = move.pop(0)
        v_num += 1
        visit[p1[0]] = 1
        move2 = []
        for i9 in range(len(move)):
            if visit[move[i9][0]] == 0:
                move2.append(move[i9])
        move = move2
        result += p1[1]
        start = p1[0]
        v1 += 1
        if v1 == V or v_num == V:
            break

    print('#{} {}'.format(ir+1, result))