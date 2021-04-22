import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 노드의 수 N+1, 간선의 수 E
    N, E = map(int, input().split())
    # 인접행렬 생성 및 입력받기
    adj_matrix = [[0]*(N+1) for x in range(N+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj_matrix[start][end] = weight
    # 0에서 부터의 비용 기록할 리스트 초기화
    cost_from_zero = [10*(N+1)]*(N+1)
    cost_from_zero[0] = 0
    # 방문여부 기록할 리스트 초기화
    visited = [0]*(N+1)
    visited[0] = 1
    # 현재 노드 설정
    current = 0
    # 방문한 노드 수 초기화
    cnt = 1
    # 다익스트라
    while cnt <= N+1:
        # cost_from_zero 갱신
        for i in range(N+1):
            # 현재 노드에서 다른 노드로 갈 수 있고, 현재 노드를 거쳐가는 것이 비용이 더 적을 때 갱신
            if adj_matrix[current][i] and cost_from_zero[current] + adj_matrix[current][i] < cost_from_zero[i]:
                cost_from_zero[i] = cost_from_zero[current] + adj_matrix[current][i]
        # 갈 수 있는 비용이 가장 낮은 노드로 current 갱신
        for i in range(N+1):
            if cost_from_zero[i] < 10*(N+1) and not visited[i]:
                current = i
                break
        for i in range(current, N+1):
            if cost_from_zero[i] < cost_from_zero[current] and not visited[i]:
                current = i
        # 방문 기록 및 방문한 노드 수 합산
        visited[current] = 1
        cnt += 1
    print("#{} {}".format(tc, cost_from_zero[N]))

