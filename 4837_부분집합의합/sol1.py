import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 부분집합 원소의 수 N, 부분집합의 합 K
    N, K = map(int, input().split())
    # 결과값을 합산한 result 변수 초기화
    result = 0
    # 모든 부분집합 생성
    for i in range(1 << 12):
        # 하나의 부분집합의 원소의 수와 그 합을 담을 임시 변수 subset_len, subset_sum 초기화
        subset_len = 0
        subset_sum = 0
        for j in range(12):
            if i & (1 << j):
                # 부분집합의 원소의 수와 합을 합산
                subset_len += 1
                subset_sum += j+1
        # 합산한 결과 원소 수가 N이고 합이 K라면 result에 1 합산
        if subset_len == N and subset_sum == K:
            result += 1
    
    print("#{} {}".format(tc, result))

