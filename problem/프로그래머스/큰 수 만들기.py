def solution(number, k):
    answer = ''
    qn = 0
    N = len(number)
    while True:
        if qn >= N - k:
            break
        if k == 0:
            answer += number[qn:]
            break
        if number[qn] == '9':
            i = 0
            while number[qn + i] == '9':
                if qn + i >= N - k:
                    break
                i += 1
            answer += '9' * i
            qn += i
        else:
            if '9' in number[qn:qn + k + 1]:
                mindex = number[qn:qn + k + 1].index('9')
            else:
                mindex = number[qn:].index(max(number[qn:qn + k + 1]))
            k -= mindex
            answer += number[qn + mindex]
            qn += mindex + 1

    return answer