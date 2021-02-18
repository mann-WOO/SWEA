import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 2차원 배열을 field에 할당
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))

    # 각 구역의 당근 수확량을 0으로 초기화
    field_up, field_right, field_down, field_left = 0, 0, 0, 0

    # 대각선: 왼쪽 위에서 오른쪽아래로 가는 대각선
    # 역대각선: 오른쪽 위에서 왼쪽 아래로 가는 대각선
    # 정중앙보다 상단의 경우
    for i in range(0, N//2):
        for j in range(N):
            # 대각선 왼쪽에 있다면 field_left에 합산
            if i + j < i + i:
                field_left += field[i][j]
            # 대각선과 역대각선 사이에 있다면 field_up에 합산
            elif i + j < i + (N-(i+1)):
                field_up += field[i][j]
            # 역대각선 오른쪽에 있다면 field_right에 합산
            else:
                field_right += field[i][j]
    # 정중앙부터 하단의 경우
    for i in range(N//2, N):
        for j in range(N):
            # 역대각선 왼쪽에 있다면 field_left에 합산
            if i + j < i + (N-(i+1)):
                field_left += field[i][j]
            # 역대각선과 대각선 사이에 있다면 field_down에 합산
            elif i + j < i + i:
                field_down += field[i][j]
            # 대각선 오른쪽에 있다면 field_right에 합산
            else:
                field_right += field[i][j]

    # 각 밭의 작업량 최대, 최소의 차이를 diff에 할당
    works = [field_up, field_right, field_down, field_left]
    max_work, min_work = field_up, field_up
    for work in works:
        if work < min_work:
            min_work = work
        elif work > max_work:
            max_work = work
    diff = max_work - min_work

    print("#{} {}".format(tc, diff))

