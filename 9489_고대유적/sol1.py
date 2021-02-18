import sys
sys.stdin = open("input.txt")
# 직사각형이기 때문에, 가로 세로를 동시에 진행 못함

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원 땅의 배열 입력받기
    ground = []
    for _ in range(N):
        ground.append(list(map(int, input().split())))
    # 가로, 세로 방향의 유물 길이를 기록할 row_len, col_len 초기화
    row_len = 0
    col_len = 0
    # 유물 중 최대 길이를 기록할 max_len 초기화
    max_len = 0

    # 가로방향 순회
    for i in range(N):
        for j in range(M):
            # 구조물이 있을 경우 row_len에 1 합산
            if ground[i][j] == 1:
                row_len += 1
            # 구조물이 없는 경우, 전까지의 구조물 길이를 확인 후 최대 길이와 비교 및 갱신
            else:
                if row_len >= 2 and row_len >= max_len:
                    max_len = row_len
                row_len = 0
        # 가로 한 줄을 돌고 마지막점에 유물이 있었다면 최대 길이와 비교 및 갱신
        if row_len >= 2 and row_len >= max_len:
            max_len = row_len
        row_len = 0

    # 세로방향 순회
    for i in range(M):
        for j in range(N):
            # 구조물이 있을 경우 col_len에 1 합산
            if ground[j][i] == 1:
                col_len += 1
            # 구조물이 없는 경우, 전까지의 구조물 길이를 확인 후 최대 길이와 비교 및 갱신
            else:
                if col_len >= 2 and col_len >= max_len:
                    max_len = col_len
                col_len = 0
        # 세로 한 줄을 돌고 마지막점에 유물이 있었다면 최대 길이와 비교 및 갱신
        if col_len >= 2 and col_len >= max_len:
            max_len = col_len
        col_len = 0

    # 최대 길이를 출력
    print("#{} {}".format(tc, max_len))

