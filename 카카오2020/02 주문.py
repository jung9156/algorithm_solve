def solution(orders, course):
    from itertools import combinations
    answer = []
    menu_list = []
    for order in orders:
        for od in order:
            if od not in menu_list:
                menu_list.append(od)
    for cour in course:
        re = {}
        for i in combinations(menu_list, cour):
            n = 0
            for ch in orders:
                for i1 in i:
                    if i1 not in ch:
                        break
                else:
                    n += 1
            re[i] = n
        re = sorted(re.items(), key = lambda x: x[1], reverse = True)
        # print(re)
        maxnum = re[0][1]
        if maxnum <= 1:
            break
        for r in re:
            word = r
            print(word)
            if r[1] == maxnum:
                answer.append(''.join(sorted(r[0])))
            elif r[1] < maxnum:
                break

    answer.sort()

    return answer