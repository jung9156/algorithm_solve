def solution(n, computers):
    answer = 0
    visit = list(-1 for i in range(n))
    visited = list(-1 for i in range(n))
    for i in range(n):
        if visit[i] == -1:
            A = [i]
            Q = []
            while True:
                if len(A) == 0:
                    for ch in Q:
                        visited[ch] = i
                    break
                v = A.pop(0)
                visit[v] = i
                for j in range(n):
                    if computers[v][j] == 1:
                        Q.append(j)
                        if visit[j] == -1:
                            A.append(j)
    Q = []
    for i in visited:
        if i not in Q:
            Q.append(i)
            answer += 1
    return answer