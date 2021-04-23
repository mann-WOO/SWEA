import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 노드의 수  N, 간선의 수 M, 인수 집 X
    N, M, X = map(int, input().split())
    # 인접행렬 입력받기
    adj_matrix = [[0] * (N + 1) for x in range(N + 1)]
    for _ in range(M):
        start, end, weight = map(int, input().split())
        adj_matrix[start][end] = weight

    # 인수 집으로 오는 비용 다익스트라
    # 인수 집으로 오는 비용 리스트 cost_to_X
    cost_to_X = [100*N]*(N+1)
    cost_to_X[X] = 0
    # 방문여부 기록할 리스트 초기화
    visited = [0]*(N+1)
    visited[X] = 1
    # 현재 노드 설정
    current = X
    # 방문한 노드 수 초기화
    cnt = 1
    # 다익스트라
    while cnt <= N:
        # cost_to_X 갱신
        # 모든 노드에 대해
        for i in range(1, N+1):
            # 다른 노드에서 현재 노드로 올 수 있고, 현재 노드를 거쳐 X로 가는 것이 기존보다 빠르다면 갱신
            if adj_matrix[i][current] and cost_to_X[current] + adj_matrix[i][current] < cost_to_X[i]:
                cost_to_X[i] = cost_to_X[current] + adj_matrix[i][current]
        # X로 올 수 있는 비용이 가장 낮은 노드로 current 갱신
        for i in range(1, N+1):
            if cost_to_X[i] < 100 * N and not visited[i]:
                current = i
                break
        for i in range(current, N+1):
            if cost_to_X[i] < cost_to_X[current] and not visited[i]:
                current = i
        # 방문 기록
        visited[current] = 1
        cnt += 1

    # 인수집에서 가는 비용 다익스트라
    # 인수 집에서 가는 비용 리스트 cost_from_X
    cost_from_X = [100 * N] * (N + 1)
    cost_from_X[X] = 0
    # 방문여부 기록할 리스트 초기화
    visited = [0] * (N + 1)
    visited[X] = 1
    # 현재 노드 설정
    current = X
    # 방문한 노드 수 초기화
    cnt = 1
    # 다익스트라
    while cnt <= N:
        # cost_from_X 갱신
        # 모든 노드에 대해
        for i in range(1, N+1):
            # 현재 노드에서 갈 수 있고, 현재 노드를 거쳐가는 비용이 기존보다 낮은 경우 갱신
            if adj_matrix[current][i] and cost_from_X[current] + adj_matrix[current][i] < cost_from_X[i]:
                cost_from_X[i] = cost_from_X[current] + adj_matrix[current][i]
        # 현재 노드에서 갈 수 있는 비용이 가장 낮은 노드로 current 갱신
        for i in range(1, N+1):
            if cost_from_X[i] < 100 * N and not visited[i]:
                current = i
                break
        for i in range(current, N + 1):
            if cost_from_X[i] < cost_from_X[current] and not visited[i]:
                current = i
        # 방문 기록
        visited[current] = 1
        cnt += 1

    # 왕복이 가장 오래 걸리는 집 찾기
    max_distance = 0
    for i in range(1, N+1):
        distance = cost_from_X[i] + cost_to_X[i]
        if distance > max_distance:
            max_distance = distance
    # 가장 오래 걸리는 거리 출력
    print("#{} {}".format(tc, max_distance))

