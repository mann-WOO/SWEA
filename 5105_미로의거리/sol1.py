import sys
sys.stdin = open("input.txt")

T = int(input())
# 델타이동 리스트
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for tc in range(1, T+1):
    N = int(input())
    maze = []
    # 미로 입력받기
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
    # visited 행렬
    visited = [[0]*N for i in range(N)]
    visited[start[0]][start[1]] = 1
    # 큐를 초기화
    q = [start]
    # 결과값 초기화(기본값: 0)
    result = 0
    # 탐색
    while q:
        # 큐에서 꺼낸 것을 현재 위치로 설정
        current_row, current_col = q.pop(0)
        # 방문 가능 영역 탐색: 네 방향
        for i in range(4):
            # 조건: maze범위 안, 벽이 아니고, 방문하지 않은 지점
            if 0 <= current_row + dr[i] < N and 0 <= current_col + dc[i] < N and maze[current_row + dr[i]][current_col + dc[i]] != 1 and visited[current_row + dr[i]][current_col + dc[i]] == 0:
                # 도착점일 때 방문 기록에 거리를 기록하고, 시작점과 종점 사이의 칸수를 result로 갱신
                if maze[current_row + dr[i]][current_col + dc[i]] == 3:
                    visited[current_row + dr[i]][current_col + dc[i]] = visited[current_row][current_col] + 1
                    result = visited[current_row + dr[i]][current_col + dc[i]] - 2
                    # 큐를 비우고 for 루프 종료 -> while 루프 종료
                    q = []
                    break
                # 도착점이 아닐 때: 방문 기록에 시작점으로부터의 거리를 기록
                else:
                    visited[current_row + dr[i]][current_col + dc[i]] = visited[current_row][current_col] + 1
                    q.append((current_row + dr[i], current_col + dc[i]))
    print("#{} {}".format(tc, result))
