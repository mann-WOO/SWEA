def bitsum(arr):
    # 1부터 시작해 공집합인 경우를 제외
    for i in range(1, 1 << 10):
        # 각 부분집합의 합을 tmp에 합산, 하나의 부분집합에서 합산이 끝나면 합을 확인
        tmp = 0
        for j in range(10):
            if i & (1 << j):
                tmp += arr[j]
        # 합산 후 tmp가 0이 된다면 1을 return
        if tmp == 0:
            return 1
    # 모든 부분집합에서 tmp가 0이 되지 않는다면 0을 return
    return 0


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    print("#{} {}".format(tc, bitsum(arr)))
