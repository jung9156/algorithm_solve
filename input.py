
import sys
sys.stdin = open('input.txt')


for ir in range(int(input())):
<<<<<<< HEAD
=======
    V, E = map(int, input().split())
    visit = list(0 for i in range(V+1))
    v_num = 0

    result = 0
    start = 0
    move = list([] for i in range(11))
    v1 = 0

    for i1 in range(E):
        i, j, w = map(int, input().split())
        move[w].append([i, j])

    flag = 0
    for i in range(len(move)):
        for j in range(len(move[i])):
            x, y = move[i][j][0], move[i][j][1]
            if visit[x] == 0 or visit[y] == 0:
                visit[x] = 1
                visit[y] = 1
                result += i
                v1 += 1
            if v1 == V:
                flag = 1
                break
        if flag == 1:
            break
    print('#{} {}'.format(ir+1, result))

>>>>>>> c84e64f251b2ce80152a356fecf2cba3a90ed0db
