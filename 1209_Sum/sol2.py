import sys
sys.stdin = open("input.txt")

T = 10
# 100*100의 arr를 input 받아 선언
for tc in range(1, T+1):
    test_case = int(input())
    arr = []
    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    # 대각선의 합
    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    # 대각선의 합을 max_value의 초기값으로 선언
    max_value = tmp

    # 반대 대각선의 합을 확인하고 max_value보다 높다면 갱신
    tmp = 0
    for i in range(100):
        tmp += arr[i][99-i]
        if tmp > max_value:
            max_value = tmp

    # row들의 합을 확인하고, max_value보다 높다면 갱신
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if tmp > max_value:
            max_value = tmp

    # col들의 합을 확인하고, max_value보다 높다면 갱신
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[j][i]
        if tmp > max_value:
            max_value = tmp

    print('#{} {}'.format(tc, max_value))
