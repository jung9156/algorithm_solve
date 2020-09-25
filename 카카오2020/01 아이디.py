def solution(new_id):
    answer = ''
    nid = ''
    #1
    for i in new_id:
        nid += i.lower()

    new_id = nid
    nid = ''

    #2
    check_l = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    for i2 in new_id:
        if i2 in check_l:
            nid += i2
    new_id = nid
    nid = ''

    #3
    q = 0
    for i3 in new_id:
        if i3 == '.':
            if q == 0:
                nid += '.'
                q = 1
        if i3 != '.':
            q = 0
            nid += i3
    new_id = nid
    nid = ''

    #4
    for i4 in range(len(new_id)):
        if i4 == 0:
            if new_id[i4] != '.':
                nid += new_id[i4]
        elif i4 == len(new_id) - 1:
            if new_id[i4] != '.':
                nid += new_id[i4]
        else:
            nid += new_id[i4]
    new_id = nid
    nid = ''

    #5
    if new_id == '':
        new_id = 'a'

    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]

    #7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id

    return answer