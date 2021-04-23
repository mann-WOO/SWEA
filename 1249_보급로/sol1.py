import sys
sys.stdin = open("input.txt")


# 델타이동 방향
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    # 2차원 배열의 길이 N
    N = int(input())
    # 각 칸의 소요시간을 기록한 board
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input()))))
    # 시작점으로부터의 소요시간을 기록한 time_from_start - 최댓값으로 초기화
    time_from_start = [[9*200]*N for x in range(N)]

    # 시작점 설정
    time_from_start[0][0] = 0
    # bfs를 위한 q와 front, rear 인덱스
    q = [(0, 0)]
    front = 0
    rear = 1

    # 변형 bfs: front가 rear와 만날 때까지
    while front < rear:
        # front의 위치를 현재 row, col 좌표로
        cr, cc = q[front]
        for i in range(4):
            # 네 방향으로 진출한 nr, nc의 좌표
            nr, nc = cr+dr[i], cc+dc[i]
            # nc, nc가 유효하고, 현재 칸에서 갔을 때 기존보다 시간이 적게 걸린다면
            if 0 <= nr < N and 0 <= nc < N and time_from_start[cr][cc] + board[nr][nc] < time_from_start[nr][nc]:
                # 시간을 갱신하고, (nr, nc)를 큐에 추가, rear를 이동
                # 한번 갔던 칸이더라도, 갱신이 되었다면 다시 방문
                time_from_start[nr][nc] = time_from_start[cr][cc] + board[nr][nc]
                q.append((nr, nc))
                rear += 1
        # front를 한 칸 뒤로 이동
        front += 1
    # 도착지까지 걸리는 시간 출력
    print("#{} {}".format(tc, time_from_start[N-1][N-1]))

