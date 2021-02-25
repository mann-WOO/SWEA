import sys
sys.stdin = open("input.txt")

def check(puzzle):
    # 델타이동 좌표
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 가로세로 검증
    for i in range(9):
        row_check = [0] * 10
        col_check = [0] * 10
        for j in range(9):
            # 퍼즐의 숫자를 이미 한번 체크 했다면 return 0
            if row_check[puzzle[i][j]] or col_check[puzzle[j][i]]:
                return 0
            else:
                row_check[puzzle[i][j]] += 1
                col_check[puzzle[j][i]] += 1
    # 9개의 정사각형 검증
    center = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
    for i, j in center:
        square_check = [0] * 10
        for k in range(8):
            # 퍼즐의 숫자를 이미 한번 체크 했다면 return 0
            if square_check[puzzle[i+dr[k]][j+dc[k]]]:
                return 0
            else:
                square_check[puzzle[i + dr[k]][j + dc[k]]] += 1
    return 1


T = int(input())
for tc in range(1, T+1):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))
    print("#{} {}".format(tc, check(puzzle)))

