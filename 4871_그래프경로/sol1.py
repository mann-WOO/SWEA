import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수 N, 간선의 개수 E
    V, E = map(int, input().split())
    # 인접행렬 adj_matrix 초기화
    adj_matrix = []
    for _ in range(V):
        adj_matrix.append([0]*V)
    # 간선을 인접행렬에 입력
    for e in range(E):
        i, j = map(int, input().split())
        adj_matrix[i-1][j-1] = 1

    # 시작점과 도착점 S,G -> -1을 해 인접행렬의 idx로 바꿔줌
    S, G = map(int, input().split())
    S, G = S - 1, G - 1

    # DFS
    # 방문 예정 노드들의 stack
    stack = []
    # 방문여부 리스트 visited
    visited = [0]*V
    # S 노드부터 시작
    stack.append(S)
    visited[S] = 1
    # 결과값 result를 0으로 초기화
    result = 0
    while stack:
        # 방문 예정 노드를 하나 꺼내 n으로 선언
        n = stack.pop()
        for i in range(V):
            # n이 가리키고 있고, 방문하지 않은 노드 중
            if adj_matrix[n][i] == 1 and visited[i] == 0:
                # G라면 result에 1 부여, stack을 비우고 for 구문 break -> while도 끝
                if i == G:
                    result = 1
                    stack = []
                    break
                # G가 아니라면 스택에 추가 및 방문 기록 후 탐색 진행
                stack.append(i)
                visited[i] = 1

    print("#{} {}".format(tc, result))

