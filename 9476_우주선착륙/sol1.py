import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    # 2차원 지형을 입력받는다.
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))

    # 주변을 탐색하기 위한 row와 col의 delta값 설정
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 적절한 위치를 기록하기 위한 변수 count 초기화
    count = 0
    # 주변부를 가질 수 있는 위치에 대해서 시행
    for i in range(1, N-1):
        for j in range(1, M-1):
            # 주변부를 확인하며 주변부의 최댓값과 최솟값 찾기
            around_max, around_min = field[i+dr[0]][j+dc[0]], field[i+dr[0]][j+dc[0]]
            for k in range(1, 8):
                if field[i+dr[k]][j+dc[k]] < around_min:
                    around_min = field[i+dr[k]][j+dc[k]]
                elif field[i+dr[k]][j+dc[k]] > around_max:
                    around_max = field[i+dr[k]][j+dc[k]]
            # 주변부의 최댓값 - 최솟값 d, 중앙과 주변부 최솟값의 차이 e
            d = around_max - around_min
            e = field[i][j] - around_min
            # 주어진 조건을 만족한다면 count에 1 합산
            if d <= K and 0 <= e <= H:
                count += 1

    print("#{} {}".format(tc, count))

