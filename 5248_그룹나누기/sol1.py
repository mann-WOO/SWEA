import sys
sys.stdin = open("input.txt")


# 연결된 노드 모두 방문하여 방문기록 남기는 dfs 함수
def dfs(k):
    visited[k] = 1
    for i in range(1, N+1):
        if adj_matrix[k][i] and not visited[i]:
            dfs(i)


T = int(input())
for tc in range(1, T+1):
    # 노드(학생) 수 N, 간선(종이) 수 M
    N, M = map(int, input().split())
    # 무방향 노드의 인접행렬 입력받기
    adj_matrix = [[0]*(N+1) for x in range(N+1)]
    edge_info = list(map(int, input().split()))
    for _ in range(M):
        frm = edge_info.pop()
        to = edge_info.pop()
        adj_matrix[frm][to] = 1
        adj_matrix[to][frm] = 1
    # 방문 기록 리스트 visited
    visited = [0]*(N+1)
    # 그래프의 수 cnt
    cnt = 0
    # 모든 노드를 확인
    for k in range(1, N+1):
        # 방문한 적 없다면, dfs로 해당 노드가 포함된 그래프 방문, cnt 1 합산
        if not visited[k]:
            dfs(k)
            cnt += 1
    print("#{} {}".format(tc, cnt))

