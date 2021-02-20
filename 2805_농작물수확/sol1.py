import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 농장 배열 문자열로 입력받기
    field = []
    for _ in range(N):
        field.append(input())
    # 가운데줄 인덱스 k
    k = N // 2
    # 결과를 합산할 변수 result
    result = 0
    # 농장의 맨 위 ~ 가운데
    for i in range(0, k+1):
        for j in range(N):
            if k-i <= j <= k+i:
                result += int(field[i][j])
    # 농장의 가운데 아래 ~ 끝
    for i in range(k+1, N):
        for j in range(N):
            if i-k <= j <= (N-1)-(i-k):
                result += int(field[i][j])

    print("#{} {}".format(tc, result))

