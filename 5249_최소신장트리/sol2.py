# Kruskal
import sys
sys.stdin = open("input.txt")


# 그래프에 연결되었다면 대표노드를, 아니라면 자기 자신을 리턴하는 함수
def find_set(x):
    if x != p[x]:
        x = p[x]
    return x


T = int(input())
for tc in range(1, T+1):
    # 마지막 노드 V(0~V), 간선의 수 E
    V, E = map(int, input().split())
    # 모든 간선 입력받는 edge 리스트: (w, n1, n2)
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))
    # 간선을 가중치 오름차순으로 정렬
    edges.sort()
    # 대표노드 리스트 p
    p = [i for i in range(V+1)]
    # 연결한 노드의 수 cnt: 첫 간선이 2개의 노드를 연결하므로 1에서 시작
    cnt = 1
    # 연결된 간선들의 가중치 합 total
    total = 0
    # 가장 비용이 낮은 간선부터 순서대로 확인
    for w, n1, n2 in edges:
        # 두 노드의 대표노드가 같지 않다면(같은 그래프에 속하지 않는다면)
        # 두 노드의 대표노드가 같다면, 사이클을 형성하므로 걸러야한다.
        if find_set(n1) != find_set(n2):
            # 현재 확인중인 간선을 채택: 노드 수 합산, 간선 가중치 합산
            cnt += 1
            total += w
            # n1을 항상 더 큰 숫자의 노드로 설정
            if n1 < n2:
                n1, n2 = n2, n1
            # 대표노드 설정: n1이 속한 그래프의 대표노드를 n2의 대표노드로
            p[find_set(n1)] = find_set(n2)
            # 모든 노드가 연결되었다면 break
            if cnt == V+1:
                break
    print("#{} {}".format(tc, total))

