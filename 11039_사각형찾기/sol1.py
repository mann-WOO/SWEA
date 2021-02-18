import sys
sys.stdin = open("input.txt")


# 사각형의 왼쪽 위 꼭지점을 찾는 함수 find_vertex
def find_vertex(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                return i, j
    return False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    # 2차원 배열 입력받기
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    max_area = 0

    # 사각형을 찾을 수 있을때까지 반복
    while find_vertex(arr, N):
        # 사각형의 너비와 높이를 0으로 초기화
        width = 0
        height = 0
        # 처음 만나는 꼭지점 찾기
        row, col = find_vertex(arr, N)
        # 너비 측정: 꼭지점에서 오른쪽으로 이동하며 0이 나올때까지 너비에 1을 합산
        current_col = col
        while arr[row][current_col] == 1:
            width += 1
            current_col += 1
        # 높이 측정: 꼭지점에서 아래로 이동하며 0이 나올때까지 높이에 1을 합산
        current_row = row
        while arr[current_row][col] == 1:
            height += 1
            current_row += 1
        # 넓이를 max_area와 비교 후 갱신
        if max_area < width * height:
            max_area = width * height
        # 찾은 사각형을 0으로 바꿔줘 삭제
        for i in range(row, row + height):
            for j in range(col, col+width):
                arr[i][j] = 0

    print("#{} {}".format(tc, max_area))
