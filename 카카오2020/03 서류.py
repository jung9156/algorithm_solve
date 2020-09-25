def solution(info, query):
    answer = []
    info_l = list(i.split(' ') for i in info)
    A = ['cpp', 'java', 'python']
    B = ['backend', 'frontend']
    C = ['junior', 'senior']
    D = ['chicken', 'pizza']
    F = [A, B, C, D]
    info_dict = dict()

    for j in A:
        if j not in info_dict:
            info_dict[j] = dict()
        for j2 in B:
            if j2 not in info_dict[j]:
                info_dict[j][j2] = dict()
            for j3 in C:
                if j3 not in info_dict[j][j2]:
                    info_dict[j][j2][j3] = dict()
                for j4 in D:
                    if j4 not in info_dict[j][j2][j3]:
                        info_dict[j][j2][j3][j4] = list()
    for i in info_l:
        info_dict[i[0]][i[1]][i[2]][i[3]].append(i[4])
    q_l = list(i.split(' ') for i in query)
    for i_list in range(len(q_l)):
        q_l[i_list] = [q_l[i_list][0], q_l[i_list][2], q_l[i_list][4], q_l[i_list][6], q_l[i_list][7]]
    result = {}
    for i2 in q_l:
        q1, q2, q3, q4, q5 = i2[0], i2[1], i2[2], i2[3], int(i2[4])
        text = q1 + q2 + q3 + q4
        if text in result.keys():
            n = 0
            for j in result[text]:
                if j >= q5:
                    n += 1
            answer.append(n)

        else:
            n = 0
            q1_l, q2_l, q3_l, q4_l = [q1], [q2], [q3], [q4]
            if q1 == '-':
                q1_l = A
            if q2 == '-':
                q2_l = B
            if q3 == '-':
                q3_l = C
            if q4 == '-':
                q4_l = D
            if q5 == '-':
                q5 = 0
            score_l = []
            for z1 in q1_l:
                for z2 in q2_l:
                    for z3 in q3_l:
                        for z4 in q4_l:
                            for i3 in info_dict[z1][z2][z3][z4]:
                                score_l.append(int(i3))
                                if int(i3) >= q5:
                                    n += 1
            answer.append(n)
            result[text] = score_l

    return answer
