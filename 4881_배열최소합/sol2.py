import sys
sys.stdin = open("input.txt")


# 백트래킹을 이용해 dfs 시간 단축
def dfs(n, k, s):
    # 순열이 완성되면 합을 sums에 추가
    if n == k:
        sums.append(s)
    # 현재 합이 합 중 최소보다 작다면 백트래킹
    elif min(sums) <= s:
        return
    # 각 행의 원소들 중 사용되지 않은 열에 대해 탐색
    else:
        for i in range(k):
            if u[i] == 0:
                u[i] = 1
                dfs(n+1, k, s+A[n][i])
                u[i] = 0


T = int(input())
for tc in range(1, T+1):
    # 배열의 크기 NxN
    N = int(input())
    # 배열 A
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    # N은 최대 10이므로 sum은 90을 넘을 수 없음
    sums = [90]
    # 사용한 열을 기록할 배열 u
    u = [0]*N
    # dfs
    dfs(0, N, 0)

    print("#{} {}".format(tc, min(sums)))

