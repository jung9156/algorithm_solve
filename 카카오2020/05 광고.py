def solution(play_time, adv_time, logs):
    answer = ''
    h, m, s = list(map(int, play_time.split(':')))
    play_time2 = h * 3600 + m * 60 + s

    h, m, s = list(map(int, adv_time.split(':')))
    adv_time2 = h * 3600 + m * 60 + s

    logs2 = list()
    for i in logs:
        i2 = list(i.split('-'))
        llog = []
        for ii2 in i2:
            tn = 0
            h, m, s = list(map(int, ii2.split(':')))
            tn += h * 3600 + m * 60 + s
            llog.append(tn)
        logs2.append(llog)


    # logs3 = []
    # for i in logs2:
    #     n1, n2 = i
    #     for i2 in range(n1, n2 + 1):
    #         if i2 not in logs3:
    #             logs3.append(i2)
    # print(logs3)


    logs3 = list()
    for u in logs2:
        logs3.append(u[0])
    logs3 += [0]
    logs3.sort()
    time_list = [0 for i in range(play_time2 + 1)]
    for i in logs2:
        t1, t2 = i
        time_list[t1:t2] = list(map(lambda x: x + 1, time_list[t1:t2]))


    re = 0
    rn = 0

    for i in logs3:
        r = sum(time_list[i:i + adv_time2])
        if r > re:
            re = r
            rn = i

    # for i in range(len(time_list) - adv_time2):
    #     if i != 0:
    #         r = sum(time_list[i:i + adv_time2])
    #         if r > re:
    #             re = r
    #             rn = i

    # r = sum(time_list[0:adv_time2])
    # ttnn = 0
    # rn = 0
    # while True:
    #     if r > re:
    #         re = r
    #         rn = ttnn
    #     if ttnn + adv_time2 == play_time2:
    #         break
    #     r -= time_list[ttnn]
    #     ttnn += 1
    #     r += time_list[ttnn + adv_time2]

    if rn // 3600 != 0:
        h = rn // 3600
        rn -= h * 3600
        h = str(h)
        if len(h) == 1:
            h = '0' + h
    else:
        h = '00'
    if rn // 60 != 0:
        m = rn // 60
        rn -= m * 60
        m = str(m)
        if len(m) == 1:
            m = '0' + m
    else:
        m = '00'
    s = str(rn)
    if len(s) == 1:
        s = '0' + s
    answer = h + ':' + m + ':' + s


    return answer



play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))