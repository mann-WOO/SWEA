import sys
sys.stdin = open("input.txt")
from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())
    # 인접행렬 adj
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
        adj[j][i] = 1
    # 시작점, 도착점
    S, G = map(int, input().split())
    result = 0
    # 방문기록 리스트
    visited = [0] * (V+1)
    # 큐
    q = [S]
    visited[S] = 1
    # bfs
    while q:
        # 큐에서 원소를 꺼내 현재 노드로 지정
        current = q.pop(0)
        # 모든 노드 중
        for i in range(1, V+1):
            # 현재 노드와 인접해 있고, 방문(예정) 기록이 없는 노드에 대해
            if adj[current][i] == 1 and visited[i] == 0:
                # 도착점이라면
                if i == G:
                    # 방문 기록에 시작점으로부터의 거리를 기록 후 거리의 차(시작점이 1이므로)를 result로 갱신
                    visited[G] = visited[current] + 1
                    result = visited[G] - visited[S]
                    # 큐를 비우고 for 루프를 종료 -> while 루프 종료
                    q = []
                    break
                # 도착점이 아니라면 방문(예정)에 거리 기록 후 큐에 추가
                else:
                    q.append(i)
                    visited[i] = visited[current] + 1
    print("#{} {}".format(tc, result))
