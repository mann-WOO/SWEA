import sys

sys.stdin = open("input.txt")


# 처음 풀이
def hamburger(n, k):
    global max_point, calorie, point
    # 칼로리가 제한을 넘었다면 백트래킹
    if calorie > L:
        return
    # 마지막 재료까지 확인했다면 점수 확인 후 max_point 갱신
    if n == k:
        if point > max_point:
            max_point = point
            return
    else:
        # 재료 넣고 다음 재료 확인
        point += Ts[n]
        calorie += Ks[n]
        hamburger(n+1, k)
        # 재료 넣지 않고 다음 재료 확인
        point -= Ts[n]
        calorie -= Ks[n]
        hamburger(n + 1, k)

T = int(input())
for tc in range(1, T + 1):
    # 재료의 수 N, 칼로리 제한 L
    N, L = map(int, input().split())
    # 재료의 맛점수 T 의 리스트 Ts, 칼로리 K의 리스트 Ks
    Ts = []
    Ks = []
    for _ in range(N):
        T, K = map(int, input().split())
        Ts.append(T)
        Ks.append(K)
    max_point = 0
    # 첫번째 재료를 넣는 경우
    point = Ts[0]
    calorie = Ks[0]
    hamburger(1, N)
    # 첫번째 재료를 넣지 않는 경우
    point = 0
    calorie = 0
    hamburger(1, N)
    print("#{} {}".format(tc, max_point))