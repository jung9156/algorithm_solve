def solution(number, k):
    answer = ''
    number = list(map(int, number))
    qn = 0
    N = len(number)
    while True:
        if qn >= N - k:
            break
        if k == 0:
            last = "".join(map(str, number[qn:]))
            answer += last
            break
        if number[qn] == 9:
            i = 0
            while number[qn + i] == 9:
                i += 1
            answer += '9' * i
            qn += i
        else:
            mindex = number[qn:].index(max(number[qn:qn + k + 1]))
            k -= mindex
            answer += str(number[qn + mindex])
            qn += mindex + 1

    return answer[:N - k]

print(solution("999991", 3))