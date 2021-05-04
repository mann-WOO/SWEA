# prim 알고리즘
import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    # 마지막 노드 V(0~V), 간선의 수 E
    V, E = map(int, input().split())
    # 인정행렬 adj_matrix
    adj_matrix = [[0]*(V+1) for x in range(V+1)]
    # 간선의 가중치 정보를 인접행렬에 입력 - 무방향
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_matrix[n1][n2] = w
        adj_matrix[n2][n1] = w
    # 현재 상태에서 각 노드의 연결비용을 기록한 costs
    costs = [11]*(V+1)
    # mst에 추가된 노드 기록할 mst
    mst = [0]*(V+1)
    # 추가한 노드의 수 기록할 cnt
    cnt = 0
    # weight의 합
    sum_weight = 0

    # 0번 노드 추가
    costs[0] = 0
    mst[0] = 1
    current = 0
    cnt += 1
    sum_costs = 0

    # 모든 노드를 추가할 때까지
    while cnt <= V:
        # costs 갱신
        for i in range(V+1):
            if adj_matrix[current][i] and adj_matrix[current][i] < costs[i]:
                costs[i] = adj_matrix[current][i]
        # 다음 연결할 노드 결정하기
        for i in range(V+1):
            if not mst[i]:
                next = i
                break
        for i in range(next, V+1):
            if costs[i] < costs[next] and not mst[i]:
                next = i
        # 노드 연결, 기록 및 비용 합산
        mst[next] = 1
        cnt += 1
        sum_costs += costs[next]
        current = next

    print("#{} {}".format(tc, sum_costs))

