import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 기차가 부딪히기까지의 시간 time
    time = D / (A + B)
    # 파리의 비행거리 result
    result = F * time
    print("#{} {}".format(tc, result))

