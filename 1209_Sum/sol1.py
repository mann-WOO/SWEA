T = 1
for tc in range(1, T+1):
    test_case = int(input())
    arr = []
    for _ in range(100):
        row = list(map(int, input()))
        arr.append(row)

    # 대각선
    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    max_value = tmp

    # 반대 대각선 -> 대각선 합을 구하는 for문에 합쳐 한번에 해결할 수도 있다.
    tmp = 0
    for i in range(100):
        tmp += arr[i][99-i]
    if tmp > max_value:
        max_value = tmp

    # row들의 합
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if tmp > max_value:
            max_value = tmp

    # col들의 합 -> row들의 합을 구하는 for문에 합쳐 한번에 해결할 수도 있다. (tmp 2개 사용)
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[j][i]
        if tmp > max_value:
            max_value = tmp

    print('#{} {}'.format(tc, max_value))