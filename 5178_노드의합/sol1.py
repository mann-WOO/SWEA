import sys
sys.stdin = open("input.txt")

T = int(input())


# 노드의 합으로 부모 노드 정하는 함수
def make_tree(node):
    # 노드 번호가 N  이상인 경우 0 반환
    if node > N:
        return 0
    # 노드 값이 0이 아닌 경우 그 값을 반환
    elif tree[node]:
        return tree[node]
    # 노드 값이 0인 경우 자식 노드들 더해서 그 값을 반환
    else:
        tree[node] = make_tree(node*2) + make_tree(node*2+1)
        return tree[node]


for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드의 수 N, 트리 구성
    tree = [0] * (N+1)
    # 리프 노드 채워주기
    for _ in range(M):
        index, val = map(int, input().split())
        tree[index] = val
    # 트리 구성
    make_tree(1)
    print("#{} {}".format(tc, tree[L]))

