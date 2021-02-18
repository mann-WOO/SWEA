import sys
sys.stdin = open("input.txt")


# yes, no 판별 함수 yes_no
def yes_no(board, N):
    # 오목 알의 진행방향 dr, dc
    dr = [-1, -1, -1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]
    # 오목판의 모든 점에 대해 확인
    for i in range(N):
        for j in range(N):
            # 오목 알이 있다면
            if board[i][j] == 'o':
                # 진행 가능한 각각의 여덟 방향별로 확인
                for k in range(8):
                    # 연속한 오목알 개수를 세는 cnt
                    cnt = 1
                    # 연속하는 오목알의 위치 설정 변수 current_row, current_col
                    current_row = i
                    current_col = j
                    # 현재 오목알의 위치에서 가능한 만큼 진행 방향으로 한 칸씩 나아가며 연속인지 확인
                    while 0 <= current_row + dr[k] < N and 0 <= current_col + dc[k] < N and board[current_row + dr[k]][current_col + dc[k]] == 'o':
                        # 연속 개수에 1을 합산
                        cnt += 1
                        # 연속하는 오목알의 위치 갱신
                        current_row = current_row + dr[k]
                        current_col = current_col + dc[k]
                        # 오목인지 확인
                        if cnt == 5:
                            return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(input())

    print("#{} {}".format(tc, yes_no(board, N)))

