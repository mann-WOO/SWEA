# 시간초과 - 백트래킹 추가로 통과

import sys
sys.stdin = open("input.txt")


# 최솟값 탐색 함수 - 시작 인덱스 (i, j), 보드 크기 N, 경로합 route_sum
def f(i, j, N, route_sum):
    global min_value
    # 마지막점 도달 시 최소합 비교 후 갱신
    if i == N - 1 and j == N - 1:
        if route_sum < min_value:
            min_value = route_sum
    else:
        # 아래로 갈 수 있을 때 이동
        if i + 1 < N:
            # 아래 확인 후 경로합에서 빼주기, 최솟값 이상일 경우 가지 않음
            route_sum += board[i+1][j]
            if route_sum < min_value:
                f(i+1, j, N, route_sum)
            route_sum -= board[i+1][j]
        # 오른쪽으로 갈 수 있을 때 이동, 최솟값 이상일 경우 가지 않음
        if j + 1 < N:
            route_sum += board[i][j+1]
            if route_sum < min_value:
                f(i, j+1, N, route_sum)


T = int(input())
for tc in range(1, T+1):
    # 보드 길이 N
    N = int(input())
    # 보드 입력받기
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    # 경로의 최소합 초기화
    min_value = N * N * 9
    # 시작점을 경로의 최소합으로 초기화
    route_sum = board[0][0]
    # 모든 경로 확인
    f(0, 0, N, route_sum)
    print("#{} {}".format(tc, min_value))

