import sys
sys.stdin = open("input.txt")


# dfs 함수
def dfs(k, cnt):
    global max_cnt
    # 방문 정점 수가 많아질 때마다 갱신
    if cnt > max_cnt:
        max_cnt = cnt
    # 방문 가능하고, 방문하지 않은 정점을 방문
    for i in range(1, N+1):
        if adj_matrix[k][i] and not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    # 정점 수 N, 간선 수 N
    N, M = map(int, input().split())
    # 인접 행렬 입력받기
    adj_matrix = []
    for _ in range(N+1):
        adj_matrix.append([0 for x in range(N+1)])
    for _ in range(M):
        frm, to = map(int, input().split())
        # 무방향 그래프
        adj_matrix[frm][to] = 1
        adj_matrix[to][frm] = 1
    # 방문한 정점 수 cnt
    cnt = 1
    # cnt의 최댓값 amx_cnt
    max_cnt = 1
    # 모든 정점에서 각각 방문기록 리스트 초기화 후 dfs 시작
    for k in range(1, N+1):
        visited = [0 for x in range(N + 1)]
        visited[k] = 1
        dfs(k, cnt)
    print("#{} {}".format(tc, max_cnt))

