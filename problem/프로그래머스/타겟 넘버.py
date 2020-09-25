def solution(numbers, target):
    answer = {}
    N = len(numbers)
    pm = ['+', '-']
    A = ['', 0]

    def find(A, k, N):
        if k == N:
            if A[1] == target and A[0] not in answer:
                answer[A[0]] = 1
            return
        else:
            for i in pm:
                if i == '+':
                    A[1] += numbers[k]
                    B = A[0]
                    A[0] += i + str(numbers[k])
                    find(A, k + 1, N)
                    A[0] = B
                    A[1] -= numbers[k]
                else:
                    A[1] -= numbers[k]
                    B = A[0]
                    A[0] += i + str(numbers[k])
                    find(A, k + 1, N)
                    A[0] = B
                    A[1] += numbers[k]

    find(A, 0, N)
    # print(answer)
    # print(len(answer))
    return len(answer)