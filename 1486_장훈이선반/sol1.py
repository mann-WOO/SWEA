import sys
sys.stdin = open("input.txt")


# 탑과 선반 높이차의 최솟값 구해주는 함수 tower
def tower(n, k, s, rs):
    global min_diff
    # 탑의 높이와 B의 차이가 min_diff보다 크거나, 남은 키를 모두 더해도 B보다 작으면 백트래킹
    if s - B > min_diff or s + rs < B:
        return
    # 마지막 사람까지 확인 했거나, 합이 선반 높이보다 높아지면 높이 차 확인 후 min_diff 갱신
    elif n == k or s > B:
        if s - B <= min_diff:
            min_diff = s - B
    # 현재 사람 탑 쌓을 때, 쌓지 않을 때로 나누어 다음 사람 확인하기
    else:
        tower(n+1, k, s+heights[n], rs-heights[n])
        tower(n+1, k, s, rs-heights[n])


T = int(input())
for tc in range(1, T+1):
    # 사람 수 N, 선반 높이 B
    N, B = map(int, input().split())
    # 사람들의 키 heights
    heights = list(map(int, input().split()))
    # 키의 합 s
    s = 0
    # 남은 사람들의 키의 합 rs
    rs = sum(heights)
    # 탑 높이와 선반 높이 차이의 최솟값 min_diff
    min_diff = rs
    tower(0, N, s, rs)
    print("#{} {}".format(tc, min_diff))

