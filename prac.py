A = list(range(0, 10))
N = 0
#N = (N + 1) % 10

#파일 선택
select_num = N
for i in range(10):
    B = []
    select_num = i
    for _ in range(4, 10):
        title_num = (select_num + _) % 10
        q = 'video' + str(title_num)
        #title_num 6번 반복
        B.append(q)
    print(B)